from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Ticket_Request
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.cache import cache

# Create your views here.
if cache.get("rem_tickets") == None:
    cache.set("rem_tickets", 100)
extra_tickets = 5
base_tickets = 6
message = 'Invalid Credentials'

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'tickets/home.html', {"available": cache.get("rem_tickets")})
    


def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login") )
    if request.method == "POST":
        users = Ticket_Request(first_name = request.POST["first"], last_name = request.POST["last"], studentID = request.POST["sid"], tickets_ordered = request.POST["base_number"], extra_tickets = request.POST["extra_number"])
        if Ticket_Request.objects.filter(studentID = request.POST['sid']):
            info = Ticket_Request.objects.get(studentID = request.POST["sid"])
            return render(request, 'tickets/registrants.html', {'info': info,
                                                                "available": cache.get("rem_tickets")})
        elif(int(request.POST["extra_number"]) > cache.get("rem_tickets")):
            return render(request, "tickets/ticket_form.html", {
                "message": "Number of Extra Tickets Ordered exceed the Number of Tickets Available, Adjust the Amount Ordered",
                "available": cache.get("rem_tickets")
            })
        users.save()
        if(int(request.POST["base_number"]) < base_tickets):
            free = cache.get("rem_tickets")  + (base_tickets - int(request.POST["base_number"]))
            free = (free - int(request.POST["extra_number"]))
            cache.set("rem_tickets", free)
        else:
            cache.set("rem_tickets", (cache.get("rem_tickets") - int(request.POST["extra_number"])))
        return render(request, 'tickets/confirm.html', {"available": cache.get("rem_tickets")})
        

    return render(request, 'tickets/ticket_form.html', {
        "base_tickets": range(1, base_tickets + 1),
        "extra_tickets": range(1, extra_tickets + 1),
        "available": cache.get("rem_tickets")
    })

def logt(request):
    logout(request)
    return render(request, 'tickets/login.html' )

def editForm(request):
    return render(request, 'tickets/registrants.html')
   
def logn(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'tickets/login.html', 
                          {"message": message})
    return render(request, 'tickets/login.html')
   
def newForm(request):
    #try: 
        user = Ticket_Request.objects.get(studentID = request.POST["id"])
        if(int(user.tickets_ordered) < base_tickets):
            new = cache.get("rem_tickets")  - (base_tickets - int(user.tickets_ordered))
            new = (new + int(user.extra_tickets))
            cache.set("rem_tickets", new)
        else:
            cache.set("rem_tickets", (cache.get("rem_tickets") + int(user.extra_tickets)))
        user.delete()
        return HttpResponseRedirect(reverse(add))
    #except Exception:
        #return render(request, 'tickets/registrants.html', {'message': "Student ID Not in Database or Typed Incorrectly", 
                                                            #"available": cache.get("rem_tickets")})



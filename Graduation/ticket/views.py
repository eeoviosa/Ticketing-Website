from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Ticket_Request
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

max_tickets = 6
message = 'Invalid Credentials'

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'tickets/home.html')
    


def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login") )
    if request.method == "POST":
        users = Ticket_Request(first_name = request.POST["first"], last_name = request.POST["last"], studentID = request.POST["sid"], tickets_ordered = request.POST["tickets_number"])
        if Ticket_Request.objects.filter(studentID = request.POST['sid']):
            return render(request, 'tickets/registrants.html', {'information':Ticket_Request.objects.get(studentID = request.POST["sid"]),
                                                                    'id' : request.POST["sid"]
                                                            })
        users.save()
        return render(request, 'tickets/confirm.html')
        

    return render(request, 'tickets/ticket_form.html', {
        "max_tickets": range(1, max_tickets + 1)
    })
def logt(request):
    logout(request)
    return render(request, 'tickets/login.html')

   
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
    try:
        user = Ticket_Request.objects.get(studentID = request.POST["id"])
        user.delete()
        return HttpResponseRedirect(reverse(add))
    except Exception:
        return render(request, 'tickets/registrants.html', {'message': "Student ID Not in Database or Typed Incorrectly"})



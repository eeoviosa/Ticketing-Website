from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Ticket_Requests
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
        users = Ticket_Requests(student_name = request.POST["name"], studentID = request.POST["studentid"], tickets_ordered = request.POST["num_of_tickets"])
        users.save()
        return render(request, 'tickets/confirm.html',
                                    {
                                        "users": Ticket_Requests.objects.all().values()
                            
                                    })
    return render(request, 'tickets/ticket_form.html', {
        "max_tickets": range(1, max_tickets + 1)
    })
def logt(request):
    return  logout(request)

   
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
   
    
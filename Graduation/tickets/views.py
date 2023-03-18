from django.shortcuts import render
from .models import Users
from django.http import HttpResponseRedirect

# Create your views here.

max_tickets = 6
def add(request):
    if request.method == "POST":
        user = Users(student_name = request.POST["name"], studentID = request.POST["studentid"], tickets_ordered = request.POST["num_of_tickets"])
        user.save()
        return render(request, 'tickets/confirm.html',
                                    {
                                        "users": Users.objects.all().values()
                            
                                    })
    return render(request, 'tickets/ticket_form.html', {
        "max_tickets": range(1, max_tickets + 1)
    })
def view(request):
   pass
def login(request):
    pass
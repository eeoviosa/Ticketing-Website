from django.shortcuts import render

# Create your views here.
max_tickets = 6
def add(request):
    return render(request, 'first/ticket_form.html', {
        "max_tickets": max_tickets
    })
def view(request):
    pass
def login(request):
    pass
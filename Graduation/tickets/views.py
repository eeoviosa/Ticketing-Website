from django.shortcuts import render

# Create your views here.
max_tickets = 6
def add(request):
    return render(request, 'tickets/ticket_form.html', {
        "max_tickets": range(1, max_tickets + 1)
    })
def view(request):
    pass
def login(request):
    pass
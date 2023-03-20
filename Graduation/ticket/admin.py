from django.contrib import admin
from .models import Ticket_Request

# Register your models here.
class TicketAdmin(admin.ModelAdmin):

    list_display = ("studentID", "first_name", "last_name", "tickets_ordered")

admin.site.register(Ticket_Request, TicketAdmin)
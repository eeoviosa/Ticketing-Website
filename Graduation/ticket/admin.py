from django.contrib import admin
from .models import Ticket_Request
from .views import base_tickets as base
from django.core.cache import cache

# Register your models here.
class TicketAdmin(admin.ModelAdmin):

    list_display = ("studentID", "first_name", "last_name", "tickets_ordered", "extra_tickets")
    action = ["delete_model"]
    #Set the admin manager as default manager
    def delete_queryset(self, request, queryset):
      for person in queryset:
        value = queryset.values_list('studentID')
        v = value[0][0]
        user = Ticket_Request.objects.get(studentID = v)
        if(int(user.tickets_ordered) < base):
            new = cache.get("rem_tickets")  - (base - int(user.tickets_ordered))
            new = (new + int(user.extra_tickets))
            cache.set("rem_tickets", new)
        else:
            cache.set("rem_tickets", (cache.get("rem_tickets") + int(user.extra_tickets)))
        queryset.delete()

admin.site.register(Ticket_Request, TicketAdmin)
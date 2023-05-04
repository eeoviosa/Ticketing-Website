from django.contrib import admin
from .models import Ticket_Request
#from .models import Multi_User
from .views import base_tickets as base
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.core.cache import cache
from .models import Student
from django.core import management
from .management.commands import importusers
import os
# Register your models here.
#Creates a admin manager class, make it a subclass for MOdelAdmin class
#class MultiAdmin(admin.ModelAdmin):
    #def save_model(self, request, obj, form, change):
        #super().save_model(request, obj, form, change)
        #file = obj.file_name
        #path = "static/"
        #absPath = os.path.join(path, "users", file)
        #management.call_command('importusers', absPath)
class TicketAdmin(admin.ModelAdmin):
#Customize values to be displayed in list form
    list_display = ("studentID", "first_name", "last_name", "tickets_ordered", "extra_tickets")
    action = ["delete_model"]

    def delete_queryset(self, request, queryset):
      for person in queryset:
        value = int(person.studentID)
        user = Ticket_Request.objects.get(studentID = value)
        if(int(user.tickets_ordered) != 0 and int(user.tickets_ordered) < base):
            new = cache.get("rem_tickets")  - (base - int(user.tickets_ordered))
            new = (new + int(user.extra_tickets))
            cache.set("rem_tickets", new)
        else:
            cache.set("rem_tickets", (cache.get("rem_tickets") + int(user.extra_tickets)))
        user.delete()
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        id = obj.studentID
        user = Ticket_Request.objects.get(studentID = id)

        if(int(user.tickets_ordered) != 0 and int(user.tickets_ordered) < base):
            new = cache.get("rem_tickets")  + (base - int(user.tickets_ordered))
            new = (new - int(user.extra_tickets))
            cache.set("rem_tickets", new)
        else:
            cache.set("rem_tickets", (cache.get("rem_tickets") - int(user.extra_tickets)))

class StudentsInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentsInline,)

#admin.site.register(Multi_User, MultiAdmin)
admin.site.register(Ticket_Request, TicketAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
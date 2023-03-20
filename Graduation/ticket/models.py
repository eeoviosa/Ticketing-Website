from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Ticket_Request(models.Model):
    tickets_ordered = models.IntegerField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64) 
    studentID = models.IntegerField(unique=True)
    

    def __str__(self):
        return f"Ticket_Ordered: {self.tickets_ordered}, First_Name: {self.first_name}, StudentID: {self.studentID} Last_Name: {self.last_name}"
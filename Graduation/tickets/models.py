from django.db import models

# Create your models here.
class Users(models.Model):
    tickets_ordered = models.IntegerField()
    student_name = models.CharField(max_length=64)
    studentID = models.IntegerField(unique=True)

    def __str__(self):
        return f"Ticket_Ordered: {self.tickets_ordered}, Student_Name: {self.student_name}, StudentID: {self.studentID}"
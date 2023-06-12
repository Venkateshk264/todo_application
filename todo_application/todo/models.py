from django.db import models

# Create your models here.
class Task(models.Model):
    Task_status_choices=(("todo","todo"),("doing","doing"),("done","done"))
    task=models.CharField(max_length=100)
    task_status=models.CharField(max_length=20,choices=Task_status_choices)
    due_date=models.DateField()
    
    def __str__(self):
        return self.task


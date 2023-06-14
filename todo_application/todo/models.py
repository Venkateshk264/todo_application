from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Task(models.Model):
    Task_status_choices=(("todo","todo"),("doing","doing"),("done","done"))
    task_title=models.CharField(max_length=100)
    task_status=models.CharField(max_length=20,choices=Task_status_choices)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    #due_date=models.DateField()
    
    def __str__(self):
        return self.task_title

    class Meta:
        ordering=["task_title"]

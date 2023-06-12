from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
   # Task_status_choices=(("todo","todo"),("doing","doing"),("done","done"))
    # task=serializers.CharField(max_length=100,required=True)
    # task_status=serializers.CharField(max_length=100)
    # due_date = serializers.DateField()

    class Meta:
        model=Task
        fields=("__all__")



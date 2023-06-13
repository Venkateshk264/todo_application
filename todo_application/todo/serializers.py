from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    task_title=serializers.CharField(max_length=100,required=True)
    task_status=serializers.CharField(max_length=100)
    #d#ue_date = serializers.DateField()


    def create(self,validated_data):
        return Task.objects.create(**validated_data)
    def update(self,instance, validated_data):
        instance.task_title=validated_data.get('task_title',instance.task_title)
        instance.task_status=validated_data.get('task_status',instance.task_status)
        #instance.due_date=validated_data.get('due_date',due_date)

        instance.save()
        return instance


    class Meta:
        model=Task
        fields=("__all__")



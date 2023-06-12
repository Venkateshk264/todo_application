from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'task_status', 'due_date')
    list_filter = ('task_status', 'due_date')
    search_fields = ('task',)


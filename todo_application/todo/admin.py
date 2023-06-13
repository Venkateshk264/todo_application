from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('task_title', 'task_status')
   # list_filter = ('task_status')
    search_fields = ('task_title',)


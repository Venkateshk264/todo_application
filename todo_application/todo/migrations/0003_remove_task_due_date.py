# Generated by Django 4.2.2 on 2023-06-13 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_rename_task_task_task_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="due_date",
        ),
    ]
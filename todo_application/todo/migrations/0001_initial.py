# Generated by Django 4.2.2 on 2023-06-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task", models.CharField(max_length=100)),
                (
                    "task_status",
                    models.CharField(
                        choices=[
                            ("todo", "todo"),
                            ("doing", "doing"),
                            ("done", "done"),
                        ],
                        max_length=20,
                    ),
                ),
                ("due_date", models.DateField()),
            ],
        ),
    ]

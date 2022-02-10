from django.db import models
import datetime


# Create your models here.
class Task(models.Model):

    def __str__(self):
        return self.name

    class Priority(models.TextChoices):
        Lowest = 'Lowest'
        Low = 'Low'
        Medium = 'Medium'
        High = 'High'
        Highest = 'Highest'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=450, blank=True)
    priority = models.CharField(max_length=7, choices=Priority.choices, default=Priority.Medium)
    date = models.DateField(default=datetime.date.today())
    done_field = models.BooleanField(default=False)
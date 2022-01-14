from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

# Create your models here
class User(AbstractUser):
    pass

class Task(models.Model):
    CATAGORIES = (
        ('A', 'Assignment'),
        ('C', 'Chore'),
        ('G', 'Goal'),
        ('C', 'Self Care'),
        ('W', 'Work'),
        ('P', 'People')
    )
    REPEATS = (
        ('N', 'Never'),
        ('H', 'Hourly'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly')
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.TextField()
    category = models.CharField(max_length=1, choices=CATAGORIES)
    # startdate = models.DateTimeField(default=timezone.now)
    # enddate = models.DateTimeField(blank=True)
    # remainingtime = models.DurationField(blank=True)
    # due = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    repeat = models.CharField(max_length=1, choices=REPEATS)

    def __str__(self):
        if (self.repeated != 'N'):
            return f"{self.title} ({self.get_catagory_display()}, Repeats {self.get_repeated_display()})"
        return f"{self.title} ({self.get_catagory_display()})"

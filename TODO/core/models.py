from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # created=models.DateField(auto_now=True)
    created=models.CharField(max_length=100)
    def __str__(self):       
        return self.task
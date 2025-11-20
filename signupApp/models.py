from django.db import models
from django.utils import timezone


# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    def published_at(self):
        self.created_at = timezone.now()
        self.save()

from django.db import models
from time import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def published_at(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name}"

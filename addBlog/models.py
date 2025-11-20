from django.db import models

# Create your models here.

class AddBlogs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')
    upload_date = models.DateField(auto_now_add=True)


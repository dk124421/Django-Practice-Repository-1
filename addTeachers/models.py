from django.db import models

# Create your models here.

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_img = models.ImageField(upload_to='teacher_images/')    
    expert_in = models.CharField(max_length=100)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.teacher_name
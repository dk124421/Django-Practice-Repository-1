from django.db import models
from time import timezone

# Create your models here.

class Courses(models.Model):
    
    course_name = models.CharField()
    rating = models.FloatField()
    duration = models.CharField()
    student_enrolled = models.IntegerField()
    course_price = models.IntegerField()
    course_image = models.ImageField(upload_to='courses_images/')   
    upload_date = models.DateTimeField(auto_now_add=True)

    
    
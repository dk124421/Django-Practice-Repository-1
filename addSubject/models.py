from django.db import models

# Create your models here.

class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    total_course = models.IntegerField()
    subject_img = models.ImageField(upload_to='subject_images/')
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject_name
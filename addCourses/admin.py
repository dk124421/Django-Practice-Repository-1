from django.contrib import admin
from addCourses.models import Courses

# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display = ("course_name", "rating", "duration", "student_enrolled", "course_price", "course_image", "upload_date")
    # search_fields = ("course_name", "rating")

admin.site.register(Courses, CoursesAdmin)
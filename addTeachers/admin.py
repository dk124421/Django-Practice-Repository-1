from django.contrib import admin
from addTeachers.models import Teachers

# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ("teacher_name", "expert_in", "teacher_img", "upload_date")


admin.site.register(Teachers, TeachersAdmin)

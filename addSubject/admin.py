from django.contrib import admin
from addSubject.models import Subjects

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_name", "total_course", "subject_img", "upload_date")
    # search_fields = ("subject_name", "total_course")

# Register your models here.
admin.site.register(Subjects, SubjectAdmin)
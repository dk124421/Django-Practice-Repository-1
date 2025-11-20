from django.contrib import admin

# Register your models here.

class AddBlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'image')

from .models import AddBlogs
admin.site.register(AddBlogs, AddBlogsAdmin)
from django.contrib import admin
from commentApp.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "website", "message", "created_at")
    # search_fields = ("name", "email", "website", "message")

admin.site.register(Comment, CommentAdmin)
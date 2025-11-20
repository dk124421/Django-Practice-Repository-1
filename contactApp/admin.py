from django.contrib import admin
from contactApp.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "subject", "created_at")
    # search_fields = ("name", "email", "message", "subject")

admin.site.register(Contact, ContactAdmin)

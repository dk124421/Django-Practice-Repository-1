from django.contrib import admin
from signupApp.models import Signup

# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "course", "password", "created_at")

# Register your models here.

admin.site.register(Signup, SignupAdmin)

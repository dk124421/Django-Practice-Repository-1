"""
URL configuration for tannu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from tannu import views

admin.site.site_header = "Tannu Admin"
admin.site.site_title = "Tannu Admin Portal"
admin.site.index_title = "Welcome to Tannu Researcher Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page, name='home_page'),
    path("about/", views.about_page, name='about_page'),
    path("contact/", views.contact_page, name='contact'),
    path("blog/", views.blog_page, name='blog_page'),
    path("course/", views.course_page, name='course_page'),
    path("teacher/", views.teacher_page, name='teacher_page'),
    path("single/", views.single_page, name='single_page'),
    path("user-data/", views.user_data, name='user_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

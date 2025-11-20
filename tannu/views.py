from commentApp.models import Comment
from django.shortcuts import render
# from django.http import HttpResponse # This import is unused
from contactApp.models import Contact
from signupApp.models import Signup
from addCourses.models import Courses
from addSubject.models import Subjects
from addTeachers.models import Teachers
from addBlog.models import AddBlogs
# from mediaApp.models import Media
from django.core.mail import send_mail
from django.template.loader import render_to_string
from tannu.settings import DEFAULT_FROM_EMAIL
import requests


def user_data(request):
	url = 'https://jsonplaceholder.typicode.com/users'
	users = []
	try:
		response = requests.get(url)
		if response.status_code == 200:
			users = response.json()
	except requests.exceptions.RequestException as e:
		print(f"Error fetching API data: {e}")
	return render(request, 'user_data.html', {'users': users})

def home_page(request):
    courses = Courses.objects.order_by('-upload_date')
    subjects = Subjects.objects.order_by('-upload_date')
    teachers = Teachers.objects.order_by('-upload_date')
    blogs = AddBlogs.objects.order_by('-upload_date')[:3] # Fetch only the 3 most recent blogs
    
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")
        password = request.POST.get("password")
 
        if not name or not email or not course or not password:
            msg = "All fields are required."
        else:
            allData = Signup(name=name, email=email, course=course, password=password)
            allData.save()
            msg = "Your form has been submitted successfully."
 
            # Send confirmation email
            reply_subject = f"Thanks for contacting us, {name}"
            html_message = render_to_string("signup_email.html", {"name": name})
            send_mail(
                reply_subject,
                "",
                DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
                html_message=html_message,
            )
            admin_subject = f"New Contact Form Submission from {name}"
            admin_message = (
                f"New message received from signup form:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Course: {course}\n"
                f"Password: {password}\n"
            )
            send_mail(
                admin_subject,
                admin_message,
                DEFAULT_FROM_EMAIL,
                [DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
    return render(request, "index.html", {"msg": msg, 'courses': courses, 'subjects': subjects, 'teachers': teachers, 'blogs': blogs})

def about_page(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")
        password = request.POST.get("password")

        if not name or not email or not course or not password:
            msg = "All fields are required."
        else:
            allData = Signup(name=name, email=email, course=course, password=password)
            allData.save()
            msg = "Your form has been submitted successfully."

            # Send confirmation email
            reply_subject = f"Thanks for contacting us, {name}"
            html_message = render_to_string("signup_email.html", {"name": name})
            send_mail(
                reply_subject,
                "",
                DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
                html_message=html_message,
            )
            admin_subject = f"New Contact Form Submission from {name}"
            admin_message = (
                f"New message received from signup form:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Course: {course}\n"
                f"Password: {password}\n"
            )
            send_mail(
                admin_subject,
                admin_message,
                DEFAULT_FROM_EMAIL,
                [DEFAULT_FROM_EMAIL],
                fail_silently=False,
                
            )
    return render(request, "about.html", {"msg": msg})

def contact_page(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        allData = Contact(name=name, email=email, subject=subject, message=message)
        allData.save()
        msg = "Your form has been submitted successfully."
        
        # Prepare reply email (plain + HTML)
        reply_subject = f"Thanks for contacting us, {name}"
        plain_message = (
            f"Dear {name},\n\n"
            "Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
            f"{message}\n\n"
            "Best regards,\n"
            "Tannu Support Team"
        )
        html_message = render_to_string("email.html", {"name": name, "message": message})

        # Send confirmation to user
        send_mail(
            reply_subject,
            plain_message,
            DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message,
        )

        # Send copy to admin
        admin_subject = f"New Contact Form Submission from {name}"
        admin_message = (
            f"New message received from contact form:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}\n"
        )
        send_mail(
            admin_subject,
            admin_message,
            DEFAULT_FROM_EMAIL,
            [DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
    return render(request, "contact.html", {"msg": msg})

def blog_page(request):
    blogs = AddBlogs.objects.order_by('-upload_date')
    return render(request, "blog.html", {'blogs': blogs})

def course_page(request):
    courses = Courses.objects.order_by('-upload_date')
    subjects = Subjects.objects.order_by('-upload_date')
    return render(request, "course.html", {'courses': courses, 'subjects': subjects})

def teacher_page(request):
    teachers = Teachers.objects.order_by('-upload_date')
    return render(request, "teacher.html", {'teachers': teachers})

def single_page(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        message = request.POST.get("message")
        # Associate comment with the blog post if your Comment model supports it
        comment = Comment(name=name, email=email, website=website, message=message)
        comment.save()
        msg = "Your comment has been posted successfully."
    return render(request, "single.html", {"msg": msg})

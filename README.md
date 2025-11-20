📘 Django Practice Repository – REST APIs, SMTP Email, Authentication & More

echo "# Django-Practice-Repository-1" 

This repository is a complete Django practice project where you learn and implement real-world backend features such as:

✔ REST API creation
✔ API calling
✔ SMTP email sending
✔ User authentication
✔ CRUD operations
✔ Working with Postman
✔ Admin panel customization
✔ Project structure & environment variables

This project is ideal for students and developers who want to practice Django by building real modules step-by-step.

🌟 Features Included
✔ REST API Development
Create APIs (GET, POST, PUT, DELETE)
DRF Serializers (if used)
JSON-based response handling

✔ API Calling
Use Python requests to call external APIs
Parse JSON
Error handling

✔ SMTP Email Sending
Gmail SMTP or custom SMTP
welcome email, custom HTML emails
Email service module

✔ Authentication System
Register / Login
Session-based auth
Custom user flow

✔ CRUD Operations
Create, Edit, Delete records
Forms + validation
Pagination & search (optional)

✔ Django Admin & Utilities
Admin customization
Model filters, search fields
Environment variables support

🛠 Tech Stack
Python
Django
Django REST Framework (optional)
SQLite / PostgreSQL
HTML, CSS, Bootstrap
SMTP
Postman (API testing)

📁 Project Structure
├───addBlog
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───addCourses
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───addSubject
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───addTeachers
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───commentApp
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───contactApp
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───media
│   ├───blog_images
│   ├───courses_images
│   ├───media
│   │   └───subject_images
│   ├───subject_images
│   └───teacher_images
├───signupApp
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───static
│   ├───css
│   ├───img
│   ├───js
│   ├───lib
│   │   ├───easing
│   │   └───owlcarousel
│   │       └───assets
│   ├───mail
│   └───scss
│       └───bootstrap
│           └───scss
│               ├───mixins
│               ├───utilities
│               └───vendor
├───tannu
│   └───__pycache__
└───templates

🚀 Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start Server
python manage.py runserver

📬 SMTP Configuration

Add to settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-app-password>'

📌 Future Enhancements
JWT Authentication
Role-based access
File upload API
Payment integration
Deployment (Render / Railway)
Caching & performance tuning

🔖 GitHub Tags (Use in Repo Settings)
django
django-practice
rest-api
smtp-email
django-learning
python-backend
django-tutorial
django-crud
api-development

🤝 Contribution
This is a learning project. Improve it, test new modules, and push updates freely.

📄 License
This project is open-source under MIT License.

📸 Screenshots (Optional)

You can upload screenshots inside /screenshots/ and display them like:
## 📸 Screenshots
### Homepage  
![Homepage](static/img/screenshots/home.png)
### Contact Page  
![Contact Page](static/img/screenshots/contact.png)
### About Page  
![About Page](static/img/screenshots/about.png)
### Single Page  
![Login Page](static/img/creenshots/single.png)
### API Test
![API Test](static/img/screenshots/api_calling.png)
### Admin Panel  
![Admin Panel](static/img/screenshots/admin.png)
### Teacher Profile  
![Teacher Profile](static/img/screenshots/teacher.png)
### Course Page  
![Course Page](static/img/screenshots/course.png)
### Blog Page  
![Blog Page](static/img/screenshots/blog.png)



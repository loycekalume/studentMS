from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main.forms import  StudentRegistrationForm
from main.models import Student


# Create your views here.
def home_view(request):
    return render(request, 'home.html')  # Make sure you have a home.html template

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm
from .models import Student


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'There was an error during registration.')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration.html', {'form': form})
# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('login')  # Redirect back to login page
    return render(request, 'login.html')
def logout_view(request):
    logout(request)  # Logout the user
    return redirect('login')  # Redirect to the login page after logout

def profile_view(request):
    # Your logic here
    return render(request, 'profile.html')

def enrollments_view(request):
    # Logic for handling enrollments
    return render(request, 'enrollments.html')

# Courses View



from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm

# View to list all courses
def course(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

# View to create a new course
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')  # Redirect to the course list after successful creation
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

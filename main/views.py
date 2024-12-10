from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main.forms import CustomUserCreationForm


# Create your views here.
def home_view(request):
    return render(request, 'home.html')  # Make sure you have a home.html template

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard after login
        else:
            messages.error(request, 'Invalid credentials')  # Show error if invalid login
    return render(request, 'login.html')

# Home view (after successful login)

# Logout view
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
def courses_view(request):
    # Logic for handling courses
    return render(request, 'courses.html')
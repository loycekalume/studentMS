"""
URL configuration for studentMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from main import views
from main.views import enroll_student

urlpatterns = [
    path('', views.home_view, name='home'),  # This maps the 'home' URL pattern
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('enrollments/', views.enrollments_list, name='enrollments'),
    path('enrollments/create/', views.create_enrollment, name='create_enrollment'),
    path('enrollments/delete/<int:pk>/', views.delete_enrollment, name='delete_enrollment'),  # Enrollments URL
    path('logout/', views.logout_view, name='logout'),
path('courses/', views.course, name='courses'),
    path('courses/create/', views.create_course, name='create_course'),
path('enroll/', enroll_student, name='enroll_student'),
    path('admin/', admin.site.urls),
]

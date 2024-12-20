from django.db import models

# Create your models here.
# models.py


# Student model extending AbstractBaseUser for custom authentication


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# models.py in your 'main' app

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.utils import timezone


class StudentManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=190, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True) # Other fields...
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'student'

    objects = StudentManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=190)
    start_date = models.DateField(null=True)
    end_date = models.DateField(default='2040-01-01')
    instructor = models.CharField(max_length=190)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name

class Enrollment(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'enrollment'
        unique_together = ('student', 'course')  # Prevent duplicate enrollments.

    def __str__(self):
        return f"{self.student} - {self.course}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

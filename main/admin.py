from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Course, Enrollment

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Student
from django.utils import timezone

class StudentAdmin(UserAdmin):
    model = Student
    list_display = ['email', 'get_full_name', 'is_active']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'get_full_name']
    ordering = ['email']

    # Add fields to display in the form, but ensure date_joined is not included
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_picture')}),  # Only add editable fields here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_picture')}),  # Same for add_fieldsets
    )

    filter_horizontal = []

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.admin_order_field = 'first_name'
    get_full_name.short_description = 'Full Name'

    def save_model(self, request, obj, form, change):
        if not obj.date_joined:
            obj.date_joined = timezone.now()  # Set date_joined to current time if not set
        super().save_model(request, obj, form, change)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    list_filter = ( 'student','enrollment_date')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course)

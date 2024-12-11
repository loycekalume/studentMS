from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from main.models import Student, Course, Enrollment, Profile

# forms.py

from django import forms
from django.contrib.auth.models import User
# forms.py

from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'username']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'instructor','start_date','end_date']



class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']  # Include student and course fields

    student = forms.ModelChoiceField(queryset=Student.objects.all(), required=True, label="Select Student")
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, label="Select Course")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

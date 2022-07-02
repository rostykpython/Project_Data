from django import forms
from .models import FileUploaded


class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = FileUploaded
        fields = ['name', 'emp_image']

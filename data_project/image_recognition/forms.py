from django import forms
from .models import FileUploaded
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FileImage(forms.ModelForm):
    class Meta: 
        model = FileUploaded
        fields = ['image', 'user']
        widgets = {
            'image': forms.widgets.FileInput(attrs={
                'class': 'form-control mb-3',
                'type': 'file',
                'id': "customFile",
                'name': 'file'

            })
        }


class CustomCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'id': 'form3Example1cg',
            'class': 'form-control form-control-lg'

        })
        self.fields['password1'].widget.attrs.update({
            'type': 'password',
            'id': 'form3Example1cg',
            'class': 'form-control form-control-lg'

        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'id': 'form3Example1cg',
            'class': 'form-control form-control-lg'

        })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'type': 'text',
                'id': 'typeUserX-2',
                'class': "form-control form-control-lg"
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'type': 'password',
                'id': 'typePasswordX-2',
                'class': "form-control form-control-lg"
            }
        )
    )

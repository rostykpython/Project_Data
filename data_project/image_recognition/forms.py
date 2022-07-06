from django import forms
from .models import FileUploaded


class FileImage(forms.ModelForm):
    class Meta: 
        model = FileUploaded
        fields = ['image', 'model']
        widgets = {
            'image': forms.widgets.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': "formFileDisabled",
                'value': ''

            })
        }
# <input type="file" class="form-control" id="customFile" />
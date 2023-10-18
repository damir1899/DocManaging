from django import forms
from django.forms import PasswordInput, TextInput, Textarea, FileInput
from django import forms
from django.contrib.auth.models import User

from .models import Document


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Username",
            }),
            "password": PasswordInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Password",
            }),
        }
        
        
class AddDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'description', 'file']
        widgets = {
            'name': TextInput(attrs={
                'class':"form-control",
                'id':"TextInput",
                'placeholder': 'Название',
                }),
            'description': Textarea(attrs={
                'class':"form-control",
                'id':"TextArea",
                'placeholder': 'Описание',
                }),
            'file': FileInput(attrs={
                'class': "form-control",
                'id': "formFile",
                }),
        }
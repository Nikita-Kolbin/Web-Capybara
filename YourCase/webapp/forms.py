from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'is_published', 'preview_img')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': "form-check form-switch"}),
            'preview_img': forms.FileInput(attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'speciality', 'about', 'link')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
            'speciality': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
        }

from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['title', 'content', 'creator', 'category', 'preview_img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'creator': forms.TextInput(attrs={'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'preview_img': forms.FileInput(attrs={'class': 'form-control'})

        }
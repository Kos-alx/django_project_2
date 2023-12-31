from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
        ]
        labels = {
            'title': 'Название',
            'text': 'Текст',
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data



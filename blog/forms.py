from django import forms 

from .models import Comment

class commentForm (forms.ModeIFrom):
    class meta:
        model = Comment
        fields = ['name', 'emall', 'Dody']
        
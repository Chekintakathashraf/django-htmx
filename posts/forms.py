from django.forms import ModelForm
from django import forms
from .models import *
class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['url','body']
        label = {
            'body': 'Caption',
        }
        widgets = {
            'url' :forms.TextInput(attrs={'placeholder':"Add Url..."}),
            'body': forms.Textarea(attrs={'row':3, 'placeholder':"Add a caption...",'class':'font1 text-2xl'})
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['body',]
        label = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'row':3, 'class':'font1 text-2xl'})
        }




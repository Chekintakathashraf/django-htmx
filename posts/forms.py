from django.forms import ModelForm
from django import forms
from .models import *
class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['url','body','tags',]
        label = {
            'body': 'Caption',
            'tags' : "Category",
        }
        widgets = {
            'url' :forms.TextInput(attrs={'placeholder':"Add Url..."}),
            'body': forms.Textarea(attrs={'row':3, 'placeholder':"Add a caption...",'class':'font1 text-2xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['body','tags',]
        label = {
            'body': '',
            'tags' : "Category",
        }
        widgets = {
            'body': forms.Textarea(attrs={'row':3, 'class':'font1 text-2xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
        label = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder':"Add body..."}),
        }

class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body',]
        label = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder':"Add reply...",'class':"!text-sm"}),
        }


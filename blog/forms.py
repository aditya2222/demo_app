from django import forms
from blog.models import *




class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('author','title','text')
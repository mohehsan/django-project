from django.forms import ModelForm
from django import forms

from .models import Photos, Comment, Categories


class PostsForm(ModelForm):
    class Meta:
        model = Photos
        fields = '__all__'
        exclude = ('comments', 'users')


class CommentForm(ModelForm):
    photo_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['text_comment']


class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

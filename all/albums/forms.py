from django import forms
from .models import Album
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("name","artist","creationDateTime","releaseDateTime","cost","isApproved")
        
        

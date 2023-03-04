from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ("name","social_links")

class UserRegister(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','password1','password2')
    
    
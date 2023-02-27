from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Artist
from django.views import View
from django.contrib.auth import login,authenticate,logout
from artists.forms import ArtistForm,UserRegister
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

class Main (View):
    def get(self,request):
        artists = Artist.objects.all()
        return render(request,'artists/base.html',{'artists':artists})

class CreateArtist(View):
    
    def get(self,request):
        form = ArtistForm()
        if not request.user.is_authenticated:
            return redirect("artists:login")

        return render(request,
                'artists/create.html',
                {'form': form})
    
    def post(self,request):
        
        form = ArtistForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect("artists:main")
        
        else:
            form = ArtistForm()
            
            return render(request,
                'artists/create.html',
                {'form': form, 'error':'error'})
            




class CreateUser(View):
    
    def get(self,request):
        registeration_form = UserRegister()
        
        return render(request, 'artists/register.html',{'registeration_form' : registeration_form})
    
    def post(self,request):
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            
            return redirect("artists:main")
        
        registeration_form = UserRegister()
        
        return render(request, 'artists/register.html',{'registeration_form' : registeration_form,'error' : 'error'})
    
    

class Login(View):
    
    def get(self,request):
        login_form = AuthenticationForm()
        return render(request,'artists/login.html', {'login_form': login_form})
    
    def post(self,request):
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                
                return redirect("artists:main")
            else:
                login_form = AuthenticationForm()
                return render(request,'artists/login.html', {'login_form': login_form, "error" : "error"})
        else:
                login_form = AuthenticationForm()
                return render(request,'artists/login.html', {'login_form': login_form, "invalid_data" : "invalid_data"})
        
            
                
class Logout(View):
    
    def get(self,request):
        logout(request)
        return redirect("artists:main")
                
        
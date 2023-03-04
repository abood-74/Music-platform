from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Artist
from django.views import View
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import  APIView
from .serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin

class Main (APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
class CreateArtist(LoginRequiredMixin,APIView):
    login_url = 'artists:login'
    
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            




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
                
        
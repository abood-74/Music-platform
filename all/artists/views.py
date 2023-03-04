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
class CreateArtist(APIView):
    
    
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

            





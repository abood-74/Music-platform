from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Album
from django.views import View
from albums.forms import AlbumForm
from django.contrib import messages
from .serializers import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CreateAlbum(APIView):
    
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        
        
            
            
            
            
            
            

    
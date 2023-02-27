from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Album
from django.views import View
from django.contrib.auth import login
from albums.forms import AlbumForm
from django.contrib import messages

class CreateAlbum(View):
    
    def get(self,request):
        form = AlbumForm()
        if not request.user.is_authenticated:
            return redirect("artists:login")

        return render(request,
                'albums/create_album.html',
                {'form': form})
    
    def post(self,request):
        
        form = AlbumForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect("albums:create")
        
        else:
            form = AlbumForm()
            
            return render(request,
                'artists/create.html',
                {'form': form, 'error':'error'})

            
            
        
        
            
            
            
            
            
            

    
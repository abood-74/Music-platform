from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album
from albums.forms import AlbumForm

def createAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return HttpResponse("ok")
        
        else:
            form = AlbumForm()
            
            return render(request,
                'albums/create_album.html',
                {'form': form, 'error':'error'})
            
            
            
            
            
            

    else:
        form = AlbumForm()

    return render(request,
                'albums/create_album.html',
                {'form': form})
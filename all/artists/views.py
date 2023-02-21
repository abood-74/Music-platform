from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Artist
from artists.forms import ArtistForm


def base(request):
    artists = Artist.objects.all()
    return render(request,'artists/base.html',{'artists':artists})


def createArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return HttpResponse("ok")
        
        else:
            form = ArtistForm()
            
            return render(request,
                'artists/create.html',
                {'form': form, 'error':'error'})
            
            
            
            
    else:
        form = ArtistForm()

    return render(request,
                'artists/create.html',
                {'form': form})
    
    
from django.urls import path
from . import views

urlpatterns = [
    path('create',views.createAlbum,name = 'create')
    
]

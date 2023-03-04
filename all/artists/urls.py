from django.urls import path
from . import views

app_name = 'artists'
urlpatterns = [
    path('create',views.CreateArtist.as_view(),name = 'create'),
    path('',views.Main.as_view(),name = 'main'),
    
    
    
]



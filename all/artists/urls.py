from django.urls import path
from . import views

urlpatterns = [
    path('create',views.createArtist,name = 'create'),
    path('',views.base,name = 'base')
]



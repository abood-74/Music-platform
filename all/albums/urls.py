from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('create',views.CreateAlbum.as_view(),name = 'create')
    
]

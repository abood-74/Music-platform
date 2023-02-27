from django.urls import path
from . import views

app_name = 'artists'
urlpatterns = [
    path('create',views.CreateArtist.as_view(),name = 'create'),
    path('',views.Main.as_view(),name = 'main'),
    path('register', views.CreateUser.as_view(), name = 'register'),
    path('login',views.Login.as_view(), name = 'login'),
    path("logout", views.Logout.as_view(), name= "logout")
    
]



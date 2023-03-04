from django.urls import path
from . import views
from knox import views as knox_views
urlpatterns = [
    path('register',views.UserCreate.as_view(), name = 'create'),
    path('login', views.LoginView.as_view(),name = 'login'),
    path('logout',knox_views.LogoutView.as_view(),name = 'logout'),
    path('logoutall',knox_views.LogoutAllView.as_view(),name = 'logout_all'),
    
    
]

from django.urls import path
from . import views 
from .views import profile_view

app_name = 'users'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', profile_view, name='profile'),

]

from django.urls import path
from . import views 
from .views import profile_view

app_name = 'users'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('profile', profile_view, name='profile'),

]

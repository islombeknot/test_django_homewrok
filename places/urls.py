from django.urls import path
from .views import places_list

app_name = 'places'


urlpatterns = [
    path('places/', places_list, name='places_list'),
]

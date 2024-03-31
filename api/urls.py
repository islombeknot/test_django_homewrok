from django.urls import path 
from .views import PlacesDetailAPIView, PlacesAPIView, ReviewsAPIView

app_name = 'api'


urlpatterns = [
     path('place_detail/<int:id>', PlacesDetailAPIView.as_view(), name='place_detail'),
     path('places/', PlacesAPIView.as_view(), name='places'),
     path('reviews/', ReviewsAPIView.as_view(), name='reviews'),


]


from django.urls import path
from .views import PlaceListView, PlaceDetailView, AddCommentView

app_name = 'places'


urlpatterns = [
    path('places/', PlaceListView.as_view(), name='place_list'),
    path('detail', PlaceDetailView.as_view(), name='place_detail'),
    path('<int:id>/comment/', AddCommentView.as_view(), name='add_comment'),
]

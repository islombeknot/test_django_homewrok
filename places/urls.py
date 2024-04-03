from django.urls import path, include 
from . import views



app_name = 'places'


urlpatterns = [
    # path('places/', PlaceListView.as_view(), name='place_list'),
    # path('detail', PlaceDetailView.as_view(), name='place_detail'),
    # path('<int:id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('', views.place_list, name='place_list'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('place/create/', views.place_create, name='place_create'),
    path('place/<int:pk>/update/', views.place_update, name='place_update'),
    path('place/<int:pk>/delete/', views.place_delete, name='place_delete'),
   

]
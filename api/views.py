from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from places.models import Place, PlaceComment
# Create your views here.


class PlacesDetailAPIView(View):
     def get(self, request, id):
          place = Place.objects.get(id=id)

          json_data = {
               "name":place.name,
               "description":place.description,      
          }
    
          return JsonResponse(json_data)

class PlacesAPIView(View):
     def get(self, request, *args, **kwargs):
          places = Place.objects.all()

          json_datas = []

          for place in places:
               json_data = {
                    "name":place.name,
                    "description":place.description
               }

               json_datas.append(json_data)
          
   
          return JsonResponse({"response":json_datas})
     
class ReviewsAPIView(View):
     def get(self, request):
          reviews = PlaceComment.objects.all()

          json_datas = []     
          for review in reviews:
               json_place = {
                    "user":{
                         "username": review.user.username,
                         "email": review.user.email,
                         "user_image": review.user.profile_image.url
                    },
                    "place":{
                         "name": review.place.name,
                         "image": review.place.image.url
                    },
                    
                    "coment": review.comment,
                    "stars_given": review.stars_given,

               }

               json_datas.append(json_place)
    
          return JsonResponse({"response":json_datas})
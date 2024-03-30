from django.shortcuts import render
from django.views import View
from places.models import PlaceComment


def landing(request):
     return render(request, 'landing_page.html')

class Homeview(View):
     def get(self, request):
        place_reviews = PlaceComment.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'place_reviews': place_reviews})
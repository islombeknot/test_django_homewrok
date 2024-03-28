from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Place

# Create your views here.

def places_list(request):
    places_list = Place.objects.all()
    paginator = Paginator(places_list, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'places_list.html', {'page_obj': page_obj})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Place, PlaceComment
from django.views.generic import DetailView, ListView
from django.views import View
from django.urls import reverse
from .forms import PlaceCommentForm
# Create your views here.





# class PlaceListView(ListView):
#     template_name = 'places_list.html'
#     queryset = Place.objects.all()
#     context_object_name = 'places'
#     paginate_by = 5
#     places_list = Place.objects.all()
#     paginator = Paginator(places_list, 1)


# def place_list(request):
#     template_name = 'places/places_list.html'
#     queryset = Place.objects.all()
#     context_object_name = 'places'
#     paginate_by = 5
#     places_list = Place.objects.all()
#     paginator = Paginator(places_list, 1)  

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_num\ber)

#     return render(request, 'places_list.html', {'page_obj': page_obj})
# class PlaceListView(View):
#     def get(self, request):
#         places = Place.objects.all().order_by('created_at')

#         search_place = request.GET.get('q', '')

#         if search_place:
#             places = places.filter(name__icontains=search_place)




#         page_size = request.GET.get("page_size", 4)
#         paginator = Paginator(places, page_size)

#         page_num = request.GET.get("page", 1)
#         page_object = paginator.get_page(page_num)

#         return render(request, 'places_list.html', context={"page_obj": page_object, "q": search_place})







# class PlaceDetailView(DetailView):
#     template_name = 'places_detail.html'
#     queryset = Place.objects.all()
#     context_object_name = 'place'
#     pk_url_kwargs = 'id'
#     form = PlaceCommentForm()
#     extra_context = {'form': form}



# def place_detail(request, place_id):
#     place = Place.objects.get(pk=place_id)
#     reviews = place.reviews.all()

#     paginator = Paginator(reviews, 5)  

#     page = request.GET.get('page')
#     try:
#         paginated_reviews = paginator.page(page)
#     except PageNotAnInteger:
        
#         paginated_reviews = paginator.page(1)
#     except EmptyPage:
       
#         paginated_reviews = paginator.page(paginator.num_pages)

#     return render(request, 'place_detail.html', {'place': place, 'paginated_reviews': paginated_reviews})

    
class AddCommentView(LoginRequiredMixin, View):

    def post(self, request, id):
      place = Place.objects.get(id=id)
      comment_form = PlaceCommentForm(data=request.POST)

      if comment_form.is_valid():
          PlaceComment.objects.create(
               place=place,
               user=request.user,
              comment=comment_form.cleaned_data['comment'],
             stars_given=comment_form.cleaned_data['stars_given']
          )
          return redirect(reverse('places:place_detail', kwargs={"id": place.id}))
      return render(request, 'place_detail.html', {"form":comment_form, "place":place} )
    


def place_list(request):
    places = Place.objects.all()
    return render(request, 'place_list.html', {'places': places})




def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'place_detail.html', {'place': place})




def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, 'place_form.html', {'form': form})


def place_update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm(instance=place)
    return render(request, 'place_form.html', {'form': form})




def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('place_list')
    return render(request, 'place_delete.html', {'place': place})


# comment crud 
def place_comment_list(request):
    comments = PlaceComment.objects.all()
    return render(request, 'places_list.html', {'comments': comments})


def place_comment_update(request, pk):
    comment = get_object_or_404(PlaceComment, pk=pk)
    if request.method == 'POST':
        form = PlaceCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceCommentForm(instance=comment)
    return render(request, 'place_comment_form.html', {'form': form})


def place_comment_delete(request, pk):
    comment = get_object_or_404(PlaceComment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('place_list')
    return render(request, 'place_comment_delete.html', {'comment': comment})


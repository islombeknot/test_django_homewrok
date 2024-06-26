from django import forms 
from .models import PlaceComment, Place

class PlaceCommentForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=1)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = PlaceComment
        fields = ['comment','stars_given']



class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description','image']

from rest_framework import serializers
from .models import PlaceComment

class PlaceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceComment
        fields = '__all__'

from django.contrib import admin
from . models import User, Place, PlaceOwner, PlaceComment, Owner 
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'description', 'adress')
     search_fields = ('id', 'name')

admin.site.register(Place, PlaceAdmin)

class OwnerAdmin(admin.ModelAdmin):
     list_display = ('id', 'first_name', 'last_name','email')
     search_fields = ('id', 'first_name')

admin.site.register(Owner, OwnerAdmin)

admin.site.register(PlaceOwner)
admin.site.register(PlaceComment)
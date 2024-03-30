from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Place(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField(null=True, blank=True)
     adress = models.CharField(max_length=255)
     image = models.ImageField(null=True, blank=True)
     created_at = models.DateTimeField(default=timezone.now)

     def __str__(self):
          return self.name
     
class Owner(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     bio = models.TextField(null=True, blank=True)
     email = models.EmailField(max_length=255)

     def __str__(self):
         return f"{self.first_name} {self.last_name}" 
     @property
     def full_name(self):
           return f"{self.first_name} {self.last_name}"
     
class PlaceOwner(models.Model):
     place = models.ForeignKey(Place, on_delete=models.CASCADE)
     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
     def __str__(self):
          return f"{self.place.name} by {self.owner.full_name}"
     
class PlaceComment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="reviews")
     comment = models.TextField()
     stars_given = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
     created_at = models.DateTimeField(default=timezone.now)

     def __str__(self):
          return f"{self.user.username} commented on {self.place.name} for {self.stars_given} stars"

     
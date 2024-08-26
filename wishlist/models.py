from django.conf import settings
from django.db import models
from destinations.models import Destination as DestinationFromDestinations


class Destination(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()
    continent = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destinations = models.ManyToManyField(DestinationFromDestinations)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

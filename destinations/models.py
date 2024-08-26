from django.db import models


class Destination(models.Model):
    CONTINENT_CHOICES = [
        ('AF', 'África'),
        ('AS', 'Ásia'),
        ('EU', 'Europa'),
        ('NA', 'América do Norte'),
        ('SA', 'América do Sul'),
        ('OC', 'Oceania'),
        ('AN', 'Antártica'),
    ]

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='destination_images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    continent = models.CharField(max_length=2, choices=CONTINENT_CHOICES)

    def __str__(self):
        return self.name

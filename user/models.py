from django.db import models

# Create your models here.
class Vehicles(models.Model):
    company_name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    registration_year = models.PositiveIntegerField(default=1)
    variant = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    fuel = models.CharField(max_length=200)
    kilometres = models.PositiveIntegerField(default=1)
    gear_type = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=1)
    colour = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    posted_date = models.CharField(max_length=200)
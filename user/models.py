from django.db import models
from django.contrib.auth.models import User

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


    def __str__(self):
        return self.company_name


class Reviews(models.Model):
    vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Wishlist(models.Model):
    vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    options = (
        ("in-wishlist","in-wishlist"),
        ("cancelled","cancelled"),
        ("order-placed","order-placed")
    )
    status = models.CharField(max_length=200,choices=options,default="in-wishlist")

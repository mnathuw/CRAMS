from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    province = models.CharField(max_length=100,default='Unknown')
    city = models.CharField(max_length = 20)
    def __str__(self):
        return self.city

class CarDealer(models.Model):
    car_dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default = 0)
    def __str__(self):
        return f"{self.car_dealer.username} - {self.area.city}"

class Vehicle(models.Model):
    car_name = models.CharField(max_length = 20)
    color = models.CharField(max_length = 10)
    dealer = models.ForeignKey(CarDealer, on_delete = models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null = True)
    capacity = models.CharField(max_length = 2)
    is_available = models.BooleanField(default = True)
    description = models.CharField(max_length = 100)
    def __str__(self):
        return f"{self.car_name}"
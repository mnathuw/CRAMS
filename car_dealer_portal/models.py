from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Area(models.Model):
    province = models.CharField(max_length=100, default='Unknown')
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

# Create your models here.
class Vehicle(models.Model):

    province_choice = (
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NL', 'Newfoundland and Labrador'),
    ('NS', 'Nova Scotia'),
    ('NT', 'Northwest Territories'),
    ('NU', 'Nunavut'),
    ('ON', 'Ontario'),
    ('PE', 'Prince Edward Island'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewan'),
    ('YT', 'Yukon'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    car_name = models.CharField(max_length=255, default="BMW")
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name='vehicles', null=True, blank=True)
    color = models.CharField(max_length=100, default='Black')
    model = models.CharField(max_length=100, default='1')
    year = models.IntegerField(('year'), choices=year_choice, default=datetime.now().year)
    dealer = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100, default='New')
    price = models.IntegerField(default=0)
    description = RichTextField(default='No description available.')
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/default.jpg')
    features = MultiSelectField(choices=features_choices, default=[])
    body_style = models.CharField(max_length=100, default='Sedan')
    engine = models.CharField(max_length=100, default='2.0L')
    transmission = models.CharField(max_length=100, default='Automatic')
    interior = models.CharField(max_length=100, default='Leather')
    miles = models.IntegerField(default=0)
    doors = models.CharField(choices=door_choices, max_length=10, default='4')
    capacity = models.IntegerField(default=5)
    vin_no = models.CharField(max_length=100, default='11111111111')
    milage = models.IntegerField(default=0)
    fuel_type = models.CharField(max_length=50, default='Gasoline')
    dealer = models.ForeignKey('CarDealer', on_delete=models.PROTECT)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_name
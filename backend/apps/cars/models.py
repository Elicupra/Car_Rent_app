from django.db import models

# # Create your models here.

fuel = [
     ('petrol', "PETROL" ), ('diesel' , 'DIESEL') , ('ev' , 'EV')
 ]
no_of_seats = range(2, 11)
transmission_types = [
    ('manual', 'MANUAL'),
    ('automatic', 'AUTOMATIC')
]


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100 , choices=fuel)
    seat_capacity = models.CharField(max_length=10, choices= no_of_seats)
    transmission_type = models.CharField(max_length=10, choices= transmission_types)
    total_km_driven = models.IntegerField()
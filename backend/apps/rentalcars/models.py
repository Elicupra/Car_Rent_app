from django.db import models

# Create your models here.
fuel = [
    ('petrol', "PETROL"),
    ('diesel', "DIESEL"),
    ('ev', "EV"),
]

no_of_seats = [
    ('2', "2 Seater"),
    ('4', "4 Seater"),
    ('5', "5 Seater"),
    ('7', "7 Seater"),
]


transmission = [
    ('manual', "Manual"),
    ('automatic', "Automatic"),
]

class Carz(models.Model):
    car_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100, choices=fuel)
    seat_capacity = models.CharField(max_length=10, choices=no_of_seats)
    transmission_type = models.CharField(max_length=20, choices=transmission)
    total_km_driven = models.PositiveIntegerField()  # total km driven
    bootspace = models.PositiveIntegerField(help_text="Bootspace in liters")
    rating = models.DecimalField(max_digits=2, decimal_places=1, help_text="Rating out of 5.0")
    car_image = models.ImageField(upload_to="rent_car_images/", blank=True, null=True)
    miliege =  models.PositiveIntegerField()

    def __str__(self):
        return self.company

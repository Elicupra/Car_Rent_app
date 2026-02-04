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
# Review Db model fields and types
categoy_choices = [
    ('SUV','SUV'),
    ('Sedan','Sedan'),
    ('Hatchback','Hatchback'),
    ('Coupe','Coupe'),
    ('Convertible','Convertible'),
    ('Minivan','Minivan'),
    ('Pickup Truck','Pickup Truck'),
]

class Carz(models.Model):
    car_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=categoy_choices, default='Sedan')
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100, choices=fuel)
    seat_capacity = models.CharField(max_length=10, choices=no_of_seats)
    transmission_type = models.CharField(max_length=20, choices=transmission)
    total_km_driven = models.PositiveIntegerField()  # total km driven
    bootspace = models.PositiveIntegerField(help_text="Bootspace in liters")
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rating out of 5.0")
    car_image = models.ImageField(upload_to="rent_car_images/", blank=True, null=True)
    mileage =  models.PositiveIntegerField() # mileage in km/l or km/kWh. Review in db model
    price_per_day = models.PositiveIntegerField(default=0) #Review in db model
    is_available = models.BooleanField(default=True) #Review in db model
    created_at = models.DateTimeField(auto_now_add=True) #Review in db model
    updated_at = models.DateTimeField(auto_now=True) #Review in db model

    def __str__(self):
        return self.company

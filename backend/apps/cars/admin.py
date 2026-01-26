"""
Docstring for backend.apps.cars.admin
"""


from django.contrib import admin
from backend.apps.cars.models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Admin configuration for Car model."""
    list_display = ('car_name', 'company','version', 'color', 'fuel_type', 'seat_capacity', 'transmission_type', 'total_km_driven','operation_type')
    search_fields = ('car_name', 'company', 'color')
    list_filter = ('fuel_type', 'transmission_type', 'seat_capacity')


@admin.update(Car)
class CarAdminUpdate(admin.ModelAdmin):
    """Updated admin configuration for Car model."""
    list_display = ('id','car_name', 'company','version', 'color', 'fuel_type', 'seat_capacity', 'transmission_type', 'total_km_driven','operation_type''')
    search_fields = ('car_name', 'company', 'color')
    list_filter = ('fuel_type', 'transmission_type', 'seat_capacity')

@admin.delete(Car)
class CarAdminDelete(admin.ModelAdmin):
    """Deleted admin configuration for Car model."""
    list_display = ('id','car_name', 'company', 'color', 'fuel_type', 'seat_capacity', 'transmission_type', 'total_km_driven','operation_type')
    search_fields = ('car_name', 'company', 'color')
    list_filter = ('fuel_type', 'transmission_type', 'seat_capacity')



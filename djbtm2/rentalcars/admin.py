from django.contrib import admin
from django.core.exceptions import ValidationError
from rentalcars.models import Carz

# Register your models here.
@admin.register(Carz)
class CarzAdmin(admin.ModelAdmin):
    # Columns visible in the admin list page
    list_display = [
        'car_name', 'company', 'category', 'fuel_type', 
        'seat_capacity', 'price_per_day', 'is_available', 'rating'
    ]

    # Filters and search    
    list_filter = ['category', 'fuel_type', 'seat_capacity', 'is_available', 'created_at']
    search_fields = ['car_name', 'company']
    readonly_fields = ['id', 'created_at', 'updated_at', 'total_km_driven']
    
    # Field organization in the admin detail page
    fieldsets = (
        ('Basic information', {
            'fields': ('car_name', 'company', 'category', 'color')
        }),
        ('Specifications', {
            'fields': ('fuel_type', 'seat_capacity', 'transmission_type', 'bootspace', 'mileage')
        }),
        ('Rentals', {
            'fields': ('price_per_day', 'is_available')
        }),
        ('Condition', {
            'fields': ('total_km_driven', 'rating', 'car_image')
        }),
        ('Audit info', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
        
    def save_model(self, request, obj, form, change):
        """Save model with validations."""
        if obj.price_per_day <= 0:
            raise ValidationError("The price per day must be a positive value.")
        if not (0 <= obj.rating <= 5.0):
            raise ValidationError("The rating must be between 0 and 5.0")
        super().save_model(request, obj, form, change)
        
        
    
from django.contrib import admin
from rentalcars.models import Carz

# Register your models here.
@admin.register(Carz)
class CarzAdmin(admin.ModelAdmin):
    # Columns visible in the admin list page
    list_display = (
        "car_name", "company","color","fuel_type","seat_capacity", 
         "transmission_type","total_km_driven","bootspace","rating",)
         
        
         
        
        
        
        
    
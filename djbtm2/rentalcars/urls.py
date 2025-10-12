from django.urls import path
from . import views

urlpatterns = [
    path("rentalcars/", views.rentalcars_view, name="rentalcars"),
    path("rental-cars/", views.rentalcars_list, name="rentalcars_list"),
    path   ("rental-car/<int:id>/", views.rentalcar_details, name="rentalcar_details"),
    path   ("rent-details/<int:id>/", views.rent_details, name="rent_details"),
    path   ("final-rent-details/<int:id>/", views.final_rent_details, name="final_rent_details"),
]

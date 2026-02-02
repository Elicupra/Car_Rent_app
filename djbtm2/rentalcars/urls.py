from django.urls import include, path
from . import views

#New imports for ViewSet

from rest_framework.routers import DefaultRouter
from rentalcars.views import CarzViewSet

router = DefaultRouter()
router.register(r'carz', CarzViewSet)

urlpatterns = [
    path("rentalcars/", views.rentalcars_view, name="rentalcars"),
    path("rental-cars/", views.rentalcars_list, name="rentalcars_list"),
    path   ("rental-car/<int:id>/", views.rentalcar_details, name="rentalcar_details"),
    path   ("rent-details/<int:id>/", views.rent_details, name="rent_details"),
    path   ("final-rent-details/<int:id>/", views.final_rent_details, name="final_rent_details"),
        # API REST
    path('api/', include(router.urls)),
]

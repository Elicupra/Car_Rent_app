"""
URL configuration for djbtm2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from btmapp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter  # New
# from rentalcars.views import CarzViewSet  # ← Add when needed

# Create router for REST API
router = DefaultRouter()
# router.register(r'carz', CarzViewSet)  # ← Se agregará cuando creemos el ViewSet
# Por ahora dejarlo vacío, se completa en el siguiente paso

urlpatterns = [
    path("",include("rentalcars.urls")),
     path("comp/",include("carsapp.urls")),     
    path("",include("btmapp.urls")),
    path('admin/', admin.site.urls),
       # API REST
    path('api/', include(router.urls)),  # ← AGREGAR ESTO
    path('api-auth/', include('rest_framework.urls')),  # ← AGREGAR ESTO (para el login de API)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

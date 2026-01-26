"""Main application file for backend."""


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from backend.apps.cars import admin,apps,models

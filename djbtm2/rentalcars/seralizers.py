from rest_framework import serializers
from rentalcars.models import Carz

class CarzListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listados (GET /api/carz/)
    Solo incluye campos esenciales para reducir payload
    """
    class Meta:
        model = Carz
        fields = [
            'id', 'car_name', 'company', 'category', 
            'fuel_type', 'seat_capacity', 'price_per_day', 
            'is_available', 'rating', 'car_image'
        ]
        read_only_fields = ['id']


class CarzDetailSerializer(serializers.ModelSerializer):
    """
    Serializer completo para detalles (GET /api/carz/{id}/)
    Incluye todos los campos para vista detallada
    """
    class Meta:
        model = Carz
        fields = [
            'id', 'car_name', 'company', 'category', 'color',
            'fuel_type', 'seat_capacity', 'transmission_type',
            'total_km_driven', 'bootspace', 'rating', 'car_image',
            'mileage', 'price_per_day', 'is_available',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total_km_driven']


class CarzCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para crear/actualizar autos (POST/PUT/PATCH)
    Incluye validaciones personalizadas
    """
    class Meta:
        model = Carz
        fields = [
            'car_name', 'company', 'category', 'color',
            'fuel_type', 'seat_capacity', 'transmission_type',
            'total_km_driven', 'bootspace', 'rating', 'car_image',
            'mileage', 'price_per_day', 'is_available'
        ]

    def validate_price_per_day(self, value):
        """Validar que precio > 0"""
        if value <= 0:
            raise serializers.ValidationError(
                "El precio por día debe ser mayor a 0"
            )
        return value

    def validate_rating(self, value):
        """Validar que rating esté entre 0 y 5.0"""
        if not (0 <= value <= 5.0):
            raise serializers.ValidationError(
                "La calificación debe estar entre 0.0 y 5.0"
            )
        return value

    def validate_mileage(self, value):
        """Validar que mileage > 0"""
        if value <= 0:
            raise serializers.ValidationError(
                "El consumo de combustible debe ser positivo"
            )
        return value
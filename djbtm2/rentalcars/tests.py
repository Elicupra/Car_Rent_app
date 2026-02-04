from django.test import TestCase
from rentalcars.models import Carz


class CarzModelTestsBasic(TestCase):
    """Tests básicos del modelo Carz"""

    def setUp(self):
        """Crear auto de prueba"""
        self.car = Carz.objects.create(
            car_name="Honda City",
            company="Honda",
            category="Sedan",
            color="Silver",
            fuel_type="petrol",
            seat_capacity="5",
            transmission_type="manual",
            total_km_driven=50000,
            bootspace=506,
            rating=4.5,
            mileage=15,
            price_per_day=500,
            is_available=True
        )

    def test_car_creation(self):
        """TEST 1: Crear auto correctamente"""
        self.assertEqual(self.car.car_name, "Honda City")
        self.assertTrue(self.car.is_available)
        self.assertEqual(self.car.price_per_day, 500)

    def test_rating_validation(self):
        """TEST 2: Rating debe estar entre 0 y 5.0"""
        self.assertGreaterEqual(self.car.rating, 0)
        self.assertLessEqual(self.car.rating, 5.0)

    def test_category_choices(self):
        """TEST 3: Categoría debe ser válida"""
        valid_categories = ['SUV', 'Sedan', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 'Pickup Truck']
        self.assertIn(self.car.category, valid_categories)

    def test_price_positive(self):
        """TEST 4: Precio debe ser positivo"""
        self.assertGreater(self.car.price_per_day, 0)

    def test_timestamps_created(self):
        """TEST 5: created_at y updated_at deben existir"""
        self.assertIsNotNone(self.car.created_at)
        self.assertIsNotNone(self.car.updated_at)

    def test_car_str_representation(self):
        """TEST 6: __str__ del auto"""
        expected = "Honda"
        self.assertEqual(str(self.car), expected)

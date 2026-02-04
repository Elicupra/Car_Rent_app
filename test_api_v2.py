#!/usr/bin/env python
"""Test API endpoints for Issue #1 - Dynamic Car Management"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"
API_BASE = f"{BASE_URL}/api"

# Test 1: GET /api/carz/ - List all cars
print("=" * 60)
print("TEST 1: GET /api/carz/ - List all cars")
print("=" * 60)
try:
    response = requests.get(f"{API_BASE}/carz/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: POST /api/carz/ - Create a new car (requires auth)
print("\n" + "=" * 60)
print("TEST 2: POST /api/carz/ - Create a new car (no auth)")
print("=" * 60)
car_data = {
    "car_name": "Honda City",
    "company": "Honda",
    "category": "Sedan",
    "color": "Black",
    "fuel_type": "petrol",
    "seat_capacity": "5",
    "transmission_type": "automatic",
    "total_km_driven": 5000,
    "bootspace": 506,
    "rating": 4.5,
    "mileage": 15,
    "price_per_day": 1500,
    "is_available": True
}
try:
    response = requests.post(f"{API_BASE}/carz/", json=car_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test 3: GET /api/carz/?category=Sedan - Filter by category
print("\n" + "=" * 60)
print("TEST 3: GET /api/carz/?category=Sedan - Filter by category")
print("=" * 60)
try:
    response = requests.get(f"{API_BASE}/carz/?category=Sedan")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("Testing complete!")
print("=" * 60)

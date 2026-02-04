#!/usr/bin/env python
"""
Script para testing de API endpoints
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8080/api/carz/"

def test_list_cars():
    """TEST 1: Listar todos los autos"""
    print("\n=== TEST 1: GET /api/carz/ (Listar autos) ===")
    try:
        response = requests.get(BASE_URL)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_create_car():
    """TEST 2: Crear un auto"""
    print("\n=== TEST 2: POST /api/carz/ (Crear auto) ===")
    try:
        car_data = {
            "car_name": "Honda City",
            "company": "Honda",
            "category": "Sedan",
            "color": "Silver",
            "fuel_type": "petrol",
            "seat_capacity": "5",
            "transmission_type": "manual",
            "total_km_driven": 50000,
            "bootspace": 506,
            "rating": 4.5,
            "mileage": 15,
            "price_per_day": 500,
            "is_available": True
        }
        response = requests.post(BASE_URL, json=car_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code in [201, 403]  # 201 si funciona, 403 si requiere auth
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_filter_category():
    """TEST 3: Filtrar por categoría"""
    print("\n=== TEST 3: GET /api/carz/?category=Sedan (Filtro) ===")
    try:
        response = requests.get(f"{BASE_URL}?category=Sedan")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_car_detail():
    """TEST 4: Obtener detalle de un auto"""
    print("\n=== TEST 4: GET /api/carz/1/ (Detalle) ===")
    try:
        response = requests.get(f"{BASE_URL}1/")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Response: {response.text}")
        return response.status_code in [200, 404]
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("TESTING API CAR RENTAL")
    print("="*60)
    
    results = {
        "TEST 1 (List)": test_list_cars(),
        "TEST 2 (Create)": test_create_car(),
        "TEST 3 (Filter)": test_filter_category(),
        "TEST 4 (Detail)": test_car_detail(),
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE TESTS")
    print("="*60)
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed = sum(results.values())
    print(f"\nTotal: {passed}/{total} tests pasaron")

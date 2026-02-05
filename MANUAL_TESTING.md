# Manual Testing Guide - Issue 2

## Environment Setup

1. **Activate Django Environment**
   ```bash
   cd d:\GitHub\Car_Rental\Car_Rent_app\djbtm2
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Apply Migration**
   ```bash
   python manage.py migrate rentalcars
   ```

## Test Case 1: Verify Migration Applied

```bash
python manage.py showmigrations rentalcars
```

**Expected Result:** `0003_carz_timestamps_rating_fix [X]` (marked as applied)

## Test Case 2: Database Schema Validation

```bash
python manage.py dbshell
```

**Run SQL (SQLite):**
```sql
PRAGMA table_info(rentalcars_carz);
```

**Expected Columns:**
- created_at (DATETIME)
- updated_at (DATETIME)
- category (VARCHAR)
- price_per_day (INTEGER)
- is_available (BOOLEAN)
- rating (DECIMAL)

## Test Case 3: Create Test Data

```bash
python manage.py shell
```

```python
from rentalcars.models import Carz
car = Carz.objects.create(
    model='Tesla Model 3',
    brand='Tesla',
    miliege=0,
    category='Sedan',
    price_per_day=100,
    is_available=True,
    rating=4.5
)
print(f"Car ID: {car.id}")
print(f"Created: {car.created_at}")
print(f"Updated: {car.updated_at}")
```

**Expected Result:** Car created with timestamps auto-populated

## Test Case 4: Test Frontend Display

```bash
python manage.py runserver
```

Access: `http://localhost:8000/admin/`

1. Navigate to Cars section
2. Create new car with:
   - Model: Test Vehicle
   - Category: SUV
   - Price/Day: 75
   - Is Available: Yes
   - Rating: 4.8

**Expected Result:** Form accepts all new fields without errors

## Test Case 5: Verify Auto-update Timestamp

```bash
python manage.py shell
```

```python
from rentalcars.models import Carz
car = Carz.objects.first()
old_updated = car.updated_at
car.price_per_day = 120
car.save()
print(f"Old updated_at: {old_updated}")
print(f"New updated_at: {car.updated_at}")
print(f"Changed: {old_updated != car.updated_at}")
```

**Expected Result:** `True` - timestamp updates on save

## Success Criteria

✅ Migration applies without errors
✅ All 5 new fields exist in database
✅ Rating field accepts decimal values (0.0-5.0)
✅ Timestamps auto-populate on creation
✅ Updated timestamp changes on modification
✅ All fields accessible in Django admin panel

---

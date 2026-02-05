# Issue 2: Database Schema Update - Timestamps & Car Rental Fields

## Migration Steps

### Prerequisites
- Ensure Django environment is activated
- Database backup recommended

### Execution Steps

1. **Navigate to project root**
   ```bash
   cd d:\GitHub\Car_Rental\Car_Rent_app\djbtm2
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate rentalcars
   ```

3. **Expected Output**
   ```
   Operations to perform:
     Apply all migrations: rentalcars
   Running migrations:
     Applying rentalcars.0003_carz_timestamps_rating_fix... OK
   ```

### Fields Added
- `created_at` - DateTimeField (auto_now_add=True)
- `updated_at` - DateTimeField (auto_now=True)
- `category` - CharField with vehicle type choices
- `price_per_day` - PositiveIntegerField
- `is_available` - BooleanField (default=True)

### Fields Modified
- `rating` - DecimalField (3 digits, 1 decimal place, max 5.0)

### Verification
```bash
python manage.py showmigrations rentalcars
```
Should show `0003_carz_timestamps_rating_fix` as applied (marked with X).

---

from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'


"""Management operations for Cars App."""
class CarsManageOperation():
    """Create Car, Update Car, Delete Car Operations for Cars App"""
    pass

    def create_car(self):
        """Create Car Operation"""
        pass
    def update_car(self):
        """Update Car Operation"""
        pass
    def delete_car(self):
        """Delete Car Operation"""
        pass

"""Type of operation: Sales/Rental"""
class OperationType():
    """Define whether the operation is Sales or Rental"""
    SALES = 'sales'
    RENTAL = 'rental'
    OPERATION_TYPE_CHOICES = [
        (SALES, 'Sales'),
        (RENTAL, 'Rental'),
    ]
    pass
    def get_operation_type(self):
        """Get Operation Type"""
        pass
    def set_operation_type(self, operation_type):
        """Set Operation Type"""
        pass

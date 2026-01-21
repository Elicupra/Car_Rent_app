from django.db import models
from btmapp.models import UserRegisteration

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    ceo = models.CharField(max_length=50)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos" ,blank=True, null=True)
    def __str__(self):
        return self.name
    
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    cc = models.IntegerField()
    milige = models.IntegerField()
    price = models.IntegerField()
    prod_image = models.ImageField(upload_to="products" ,blank=True, null=True)
    

    Company = models.ForeignKey(Company,related_name="companies", on_delete=models.CASCADE)  # act as forign key 
    def __str__(self):
        return self.product_name
    
    
# class ProductInteriorImgs(models.Model):
#     interior = models.ImageField(upload_to="interior" ,blank=True, null=True)
#     product= models.ForeignKey(Products,related_name='products', on_delete=models.CASCADE)
    
    
# class ProductExteriorImgs(models.Model):
#     exterior = models.ImageField(upload_to="exterior" ,blank=True, null=True)
#     product= models.ForeignKey(Products,related_name='products', on_delete=models.CASCADE)
    
    
class ProductInteriorImgs(models.Model):
    interior = models.ImageField(upload_to="interior", blank=True, null=True)
    product = models.ForeignKey(
        Products,
        related_name='interior_images',
        on_delete=models.CASCADE
    )

class ProductExteriorImgs(models.Model):
    exterior = models.ImageField(upload_to="exterior", blank=True, null=True)
    product = models.ForeignKey(
        Products,
        related_name='exterior_images',
        on_delete=models.CASCADE
    )




class Book_Test_Drive(models.Model):
    product_name = models.ForeignKey(
        Products,
        related_name='booked_test_drives',
        on_delete=models.CASCADE
    )
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    t_date = models.DateField()
    time_slot = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
    
    
    
# class Enquiry(models.Model):
#     user_name  = models.ForeignKey(UserRegisteration, on_delete=models.CASCADE)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     concern = models.CharField(max_length=500)
    
    
    

    
 

class Enquiry(models.Model):
    user = models.ForeignKey(UserRegisteration, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50) 
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    concern = models.CharField(max_length=500)
    def __str__(self):
        return self.user.user.username
    
    
    
    


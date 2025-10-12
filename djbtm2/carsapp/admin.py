from django.contrib import admin
from carsapp.models import Company, Products, ProductInteriorImgs, ProductExteriorImgs,Book_Test_Drive,Enquiry
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'ceo', 'est_year', 'origin'] 
   

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name',"color","seat_capacity","fuel_type", "cc","milige",'Company',]  
    
class ProductInteriorImgsAdmin(admin.ModelAdmin):
    list_display = ["interior",'product']
    
class ProductExteriorImgsAdmin(admin.ModelAdmin):
    list_display = ["exterior",'product']
   
   
class BookTestDriveAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'product_name', 'email', 'phone', 't_date', 'time_slot']

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'phone' , "concern"]
    search_fields = ['user_name', 'email', 'phone']
    list_filter = ['user_name']
admin.site.register(Company, CompanyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductInteriorImgs, ProductInteriorImgsAdmin)
admin.site.register(ProductExteriorImgs, ProductExteriorImgsAdmin)
admin.site.register(Book_Test_Drive,BookTestDriveAdmin)
admin.site.register(Enquiry,EnquiryAdmin)






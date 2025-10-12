from django import forms
from carsapp.models import Products, Book_Test_Drive,Enquiry

class ProductEmiForm(forms.ModelForm):
    product_name=forms.CharField(disabled=True)
    price=forms.CharField(disabled=True)
    class Meta:
        model=Products
        fields=['product_name','price']
    loan_amount=forms.IntegerField()
    tensure=forms.IntegerField()
    
  


from django import forms
from carsapp.models import Products, Book_Test_Drive, Enquiry

class Test_Drive_Form(forms.ModelForm):
    product_name = forms.CharField(disabled=True)
    user_name = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)
    phone = forms.CharField(disabled=True)
    t_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    time_slot = forms.ChoiceField(
        choices=[
            ('9AM - 11AM', '9AM - 11AM'),
            ('11AM - 1PM', '11AM - 1PM'),
            ('2PM - 4PM', '2PM - 4PM'),
            ('4PM - 6PM', '4PM - 6PM'),
        ],
        required=True
    )

    class Meta:
        model = Book_Test_Drive
        # Add 'phone' to the fields list
        fields = ['user_name','email','phone', 't_date', 'time_slot']
        
# class Enquiry_Form(forms.ModelForm):
#     user_name = forms.CharField(disabled=True)
#     phone = forms.CharField(disabled=True)
#     email = forms.CharField(disabled=True)
#     concern = forms.CharField()
#     class Meta:
#         model = Enquiry
#         fields = ['concern']
    

class Enquiry_Form(forms.ModelForm):
    user_name = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)
    phone = forms.CharField(disabled=True)
    concern = forms.CharField()

    class Meta:
        model = Enquiry
        fields = ["user_name","email","phone","concern"]  

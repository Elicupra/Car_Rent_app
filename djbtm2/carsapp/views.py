from django.shortcuts import render, get_object_or_404,redirect 
from carsapp.models import Company,Products
from btmapp.models import UserRegisteration  
from django.contrib.auth.decorators import login_required
from carsapp.forms import ProductEmiForm,Test_Drive_Form,Enquiry_Form
from btmapp.forms import UserForm,UserProfileForm,userUpdateForm,UserProfileUpdateForm
import math
# Create your views here.

@login_required(login_url="login")
def company_list(request):
    comp_name = Company.objects.all()
    
    context = {
        "comp_name": comp_name
    }
    return render(request,"cars/CompanyList.html",context)
    
  
@login_required(login_url="login")
def company_details(request , id= 0):
    company = Company.objects.get(id = id)
    print(company)
    return render(request, "cars/companydetails.html", {"company":company})
      
      
      

@login_required(login_url='login')
def calcemi(request, id=0):
    product = Products.objects.get(id=id)
    emi = None

    if request.method == 'POST':
        form = ProductEmiForm(request.POST, instance=product)
        if form.is_valid():
            price = form.cleaned_data.get('price') or 0
            print(price)
            loan_amount = form.cleaned_data.get('loan_amount') or 0
            print(loan_amount)
            tenure = form.cleaned_data.get('tensure') or 0  # in years
            print(tenure)

            # Auto-set interest rates based on tenure
            if 1 <= tenure <= 2:
                interest_rate = 8.5
            elif 3 <= tenure <= 4:
                interest_rate = 9.5
            elif 5 <= tenure <= 6:
                interest_rate = 10.5
            elif 7 <= tenure <= 8:
                interest_rate = 12
            elif tenure >= 9:
                interest_rate = 13.5
            else:
                interest_rate = 10.0

            try:
                loan_amount = float(loan_amount)
                tenure = int(tenure)
                interest_rate = float(interest_rate)

                monthly_rate = interest_rate / 12 / 100
                total_months = tenure * 12

                if loan_amount > 0 and monthly_rate > 0:
                    emi = (loan_amount * monthly_rate * math.pow(1 + monthly_rate, total_months)) / \
                          (math.pow(1 + monthly_rate, total_months) - 1)
                    emi = round(emi, 2)
            except (TypeError, ValueError, ZeroDivisionError):
                emi = None
    else:
        form = ProductEmiForm(instance=product)

    return render(request, 'cars/emi.html', {'form': form, 'emi': emi})





@login_required(login_url="login")
def product_detail(request, id=0):
    product = Products.objects.get(id=id)   
    interior_images = product.interior_images.all()
    exterior_images = product.exterior_images.all()

    context = {
        "product": product,
        "interior_images": interior_images,
        "exterior_images": exterior_images
    }
    return render(request, "cars/product_detail.html", context)


 
@login_required(login_url="login")
def final_price(request, id=0):
    product = Products.objects.get(id=id)
    price = product.price  

    
    road_tax = round(price * 0.08, 2)          
    rto_charges = round(price * 0.05, 2)       
    gst = round(price * 0.18, 2)               
    insurance = round(price * 0.035, 2)       
    misc = round(price * 0.02, 2)              

    final_price = round(price + road_tax + rto_charges + gst + insurance + misc, 2)

    context = {
        "product": product,
        "road_tax": road_tax,
        "rto_charges": rto_charges,
        "gst": gst,
        "insurance": insurance,
        "misc": misc,
        "final_price": final_price,
    }
    return render(request, "cars/product_final_price.html", context)





@login_required(login_url="login")
def Book_Test_Drive_views(request, id=0):
    product = Products.objects.get(id=id)

    if request.method == "POST":
        form = Test_Drive_Form(request.POST,  initial={
                "product_name": product.product_name,
                "user_name": request.user.username,
                "email": request.user.email,
                "phone": request.user.userregisteration.phone
            })
        if form.is_valid():
            test_drive = form.save(commit=False)
            test_drive.product_name = product  
            test_drive.user = request.user.userregisteration 
            test_drive.save()
            return render(
                request,
                "cars/book_test_drive.html",
                {"confirmed": True, "product": product}
            )
    else:
        form = Test_Drive_Form(initial={
            "product_name": product.product_name,
            "user_name": request.user.username,
            "email": request.user.email,
            "phone": request.user.userregisteration.phone
        })

    return render(request, "cars/book_test_drive.html", {"form": form, "product": product})


@login_required(login_url="login")
def enquiry_view(request, id=0):
     product = Products.objects.get(id=id)
     if request.method == "POST":
        form = Enquiry_Form(request.POST, initial={
            
            "user_name": request.user.username,
            "email": request.user.email,
            "phone": request.user.userregisteration.phone
        })
        if form.is_valid():
            enquiry = form.save(commit=False)
              
            enquiry.user_name = request.user.username
            enquiry.user = request.user.userregisteration
            enquiry.save()
            return render(
                request,
                "cars/enquiry.html",
                {"confirmed": True, "product": product}
            )
     else:
        form = Enquiry_Form(initial={
            
            "user_name": request.user.username,
            "email": request.user.email,
            "phone": request.user.userregisteration.phone
        })

        return render(request, "cars/enquiry.html", {"form": form,"product": product})
    

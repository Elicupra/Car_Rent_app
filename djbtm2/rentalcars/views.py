from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rentalcars.models import Carz
from rentalcars.forms import RentDetailsForm, FinalRentDetailsForm
from btmapp.utils import send_email_view

# Create your views here.


@login_required(login_url="login")
def rentalcars_view(request):
    return render(request, "rental/rentalcars.html")


#  car list
@login_required(login_url="login")
def rentalcars_list(request):
    seat_capacity = request.GET.get("seat", None)  # check if seat filter is passed

    if seat_capacity:
        cars = Carz.objects.filter(seat_capacity=seat_capacity)
    else:
        cars = Carz.objects.all()  # show all if no filter

    return render(
        request,
        "rental/rental_car_image.html",
        {"cars": cars, "seat_capacity": seat_capacity},
    )


#  Rent Details
@login_required(login_url="login")
def rentalcar_details(request, id=0):
    car = Carz.objects.get(id=id)
    return render(request, "rental/rental_car_details.html", {"car": car})


def rent_details(request, id=0):
    car = Carz.objects.get(id=id)
    amount_per_km = 0

    # Determine rate per km
    if car.fuel_type == "petrol" and car.seat_capacity == "5":
        amount_per_km = 11
    elif car.fuel_type == "petrol" and car.seat_capacity == "7":
        amount_per_km = 16
    elif car.fuel_type == "ev" and car.seat_capacity == "5":
        amount_per_km = 11
    elif car.fuel_type == "ev" and car.seat_capacity == "7":
        amount_per_km = 16
    elif car.fuel_type == "diesel" and car.seat_capacity == "5":
        amount_per_km = 9
    elif car.fuel_type == "diesel" and car.seat_capacity == "7":
        amount_per_km = 14

    total_amount = None

    if request.method == "POST":
        form = RentDetailsForm(request.POST)
        if form.is_valid():
            total_no_days = form.cleaned_data["total_no_days"]
            expected_km = form.cleaned_data["expected_km"]

            # Minimum chargeable km = 300 per day
            min_chargeable_km = 300 * total_no_days
            chargeable_km = max(expected_km, min_chargeable_km)

            total_amount = chargeable_km * amount_per_km
    else:
        form = RentDetailsForm()

    return render(
        request,
        "rental/rent_details.html",
        {
            "car": car,
            "form": form,
            "amount_per_km": amount_per_km,
            "total_amount": total_amount,
        },
    )


def final_rent_details(request, id=0):
    car = Carz.objects.get(id=id)
    loggedin_user_email = request.user.email
    print(loggedin_user_email)
    amount_per_km = 0

    # rate per km
    if car.fuel_type == "petrol" and car.seat_capacity == "5":
        amount_per_km = 11
    elif car.fuel_type == "petrol" and car.seat_capacity == "7":
        amount_per_km = 16
    elif car.fuel_type == "ev" and car.seat_capacity == "5":
        amount_per_km = 11
    elif car.fuel_type == "ev" and car.seat_capacity == "7":
        amount_per_km = 16
    elif car.fuel_type == "diesel" and car.seat_capacity == "5":
        amount_per_km = 9
    elif car.fuel_type == "diesel" and car.seat_capacity == "7":
        amount_per_km = 14

    # final_price = None
    # raw_total = None
    # fuel_cost = None
    # travelled_km = None
    final_price = 0
    raw_total = 0
    fuel_cost = 0
    travelled_km = 0

    if request.method == "POST":
        form = FinalRentDetailsForm(request.POST)

        if form.is_valid():
            total_no_days = form.cleaned_data["total_no_days"]
            km_drive_now = form.cleaned_data["km_drive_now"]

            # Calculate travelled distance
            travelled_km = km_drive_now - car.total_km_driven

            # Minimum chargeable distance
            min_chargeable_km = 300 * total_no_days

            # If driven more than allowed
            if travelled_km > min_chargeable_km:
                extra_km = travelled_km - min_chargeable_km
            else:
                extra_km = 0

            # Base rental calculation
            raw_total = travelled_km * amount_per_km

            # Add percentage based on extra km
            if extra_km > 0:
                if extra_km < 500:
                    raw_total += raw_total * 0.02
                else:
                    raw_total += raw_total * 0.04

            # Fuel cost calculation
            fuel_price_per_litre = 102  # fixed as per your requirement

            fuel_needed = travelled_km / car.miliege  # use miliege instead of mileage

            fuel_cost = fuel_needed * fuel_price_per_litre

            # Final price = rental - fuel cost
            final_price = raw_total - fuel_cost
            response = send_email_view(loggedin_user_email)
            print("email sent")
            return response
    else:
        form = FinalRentDetailsForm()
        print()

    return render(
        request,
        "rental/final_rent_details.html",
        {
            "car": car,
            "form": form,
            "amount_per_km": amount_per_km,
            "final_price": final_price,
            "raw_total": raw_total,
            "fuel_cost": fuel_cost,
            "travelled_km": travelled_km,
        },
    )

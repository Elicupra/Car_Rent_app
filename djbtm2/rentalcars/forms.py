from django import forms
from rentalcars.models import Carz

class RentDetailsForm(forms.Form):
    total_no_days = forms.IntegerField(
        label="Total Number of Days",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter number of days"}
        ),
    )
    expected_km = forms.IntegerField(
        label="Expected KM",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter expected KM"}
        ),
    )


class FinalRentDetailsForm(forms.Form):
    total_no_days = forms.IntegerField(
        label="Total Number of Days",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    km_drive_now = forms.IntegerField(
        label="Km Driven Till Now (ODO Reading)",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class CarzForm(forms.ModelForm):
    class Meta:
        model = Carz
        fields = '__all__'
    
    def clean_price_per_day(self):
        price = self.cleaned_data.get('price_per_day')
        if price and price <= 0:
            raise forms.ValidationError("The price per day must be positive")
        return price
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and not (0 <= rating <= 5.0):
            raise forms.ValidationError("The rating must be between 0 and 5.0")
        return rating
    
    def toggle_availability(self, request, queryset):
        count = queryset.update(is_available=~F('is_available'))
        self.message_user(request, f"{count} autos actualizados")
    toggle_availability.short_description = "Toggle availability"

    actions = [toggle_availability]
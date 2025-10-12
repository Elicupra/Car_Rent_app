from django import forms


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
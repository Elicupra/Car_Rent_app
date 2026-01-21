from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from btmapp.models import UserRegisteration


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username", "email", "password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegisteration
        fields = [
            "phone",
            "door_no",
            "street",
            "landmark",
            "city",
            "state",
            "pincode",
            "userpic",
        ]

    captcha = ReCaptchaField()


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserRegisteration
        fields = [
            "phone",
            "door_no",
            "street",
            "landmark",
            "city",
            "state",
            "pincode",
            "userpic",
        ]


class PasswordResetForm(forms.Form):
    username = forms.CharField(label="User Name", required=True)
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label="Confirm Password", required=True, widget=forms.PasswordInput
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data


# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>user details</title>
#   </head>
#   <body>
#     <h1>Registeration Form</h1>
#     {{ form.as_p }}
#     {{ form1.as_p }}
#     <input type="submit" value="REGISTER" />
#   </body>
# </html>

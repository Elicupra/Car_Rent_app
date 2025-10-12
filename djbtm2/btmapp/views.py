from django.shortcuts import render, redirect
from btmapp.forms import (
    UserForm,
    UserProfileForm,
    userUpdateForm,
    UserProfileUpdateForm,
    PasswordResetForm,
)
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def registeration(request):
    registered = False
    if request.method == "POST":
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST, request.FILES)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

    else:
        form = UserForm()
        form1 = UserProfileForm()

    context = {"form": form, "form1": form1, "registered": registered}

    return render(request, "registeration.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("home")
        else:
            return HttpResponse("pls check your cred ")
    return render(request, "login.html", {})


@login_required(login_url="login")
def home(request):
    return render(request, "home.html", {})


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def profile(request):
    return render(request, "profile.html", {})


@login_required(login_url="login")
def update(request):
    if request.method == "POST":
        form = userUpdateForm(request.POST, instance=request.user)
        form1 = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userregisteration
        )

        if form.is_valid() and form1.is_valid():
            user = form.save()
            form1.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("profile")

    else:
        form = userUpdateForm(instance=request.user)
        form1 = UserProfileUpdateForm(instance=request.user.userregisteration)
    return render(request, "update.html", {"form": form, "form1": form1})


# def PasswordReset(request):
#     if request.method == "POST":
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             confirm_password = request.POST["confirm_password"]
#             print(username)
#             print(password)
#             print(confirm_password)
#         else:
#             form = PasswordResetForm()

#     return render(request, "password_reset.html", {"form" : form})

def PasswordReset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            new_password = form.cleaned_data["password"]
            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                return redirect("login")
            except User.DoesNotExist:
                return HttpResponse("<h1>User does not exist</h1>")
    else:
        form = PasswordResetForm()

    return render(request, "password_reset.html", {"form": form})



# BY sir

# from django.shortcuts import render
# from btmapp.forms import UserForm,UserProfileForm
# # Create your views here.
# def registeration(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         form1= UserProfileForm(request.POST,request.FILES)
#         if form.is_valid() and form1.is_valid() :
#             print(form.cleaned_data["username"])
#             print(form1.cleaned_data["city"])
#     else:
#         form = UserForm()
#         form1= UserProfileForm()


#     context = {
#         "form" : form,
#         'form1':form1
#     }

#     return render(request,"registeration.html",context)


# By sir 1st view made by sir

# from django.shortcuts import render
# from btmapp.forms import UserForm,UserProfileForm
# # Create your views here.


# def registeration(request):
#     form = UserForm()
#     form1= UserProfileForm()
#     context = {
#         "form" : form,
#         'form1':form1
#     }
#     return render(request,"registeration.html",context)


#  By me  But IT is wrong

# def registeration(request):
#     form = UserForm()
#     form1= UserProfileForm()
#     context = {
#         "form" : form,
#         'form1':form1
#     }
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         form1 = UserProfileForm(request.POST)
#         if form.is_valid() and form1.is_valid() :
#             print("validation Scuccess")
#             form.save()# work only u have created the model forms
#             print(form.cleaned_data["username"], form1.cleaned_data["phone"])
#     return render(request,"registeration.html",context)


# written by me only but is also wrong

# from django.shortcuts import render
# from btmapp.forms import UserForm,UserProfileForm
# # Create your views here.


# def registeration(request):
#     form = UserForm()
#     form1= UserProfileForm()
#     context = {
#         "form" : form,
#         'form1':form1
#     }
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         form1 = UserProfileForm(request.POST)
#         if form.is_valid() and form1.is_valid() :
#             print("validation Scuccess")
#             form.save()# work only u have created the model forms
#             print(form.cleaned_data["username"], form1.cleaned_data["phone"])
#     return render(request,"registeration.html",context)


# from django.shortcuts import render
# from btmapp.forms import UserForm,UserProfileForm
# # Create your views here.


# def registeration(request):
#     form = UserForm()
#     form1= UserProfileForm()
#     context = {
#         "form" : form,
#         'form1':form1
#     }
#     return render(request,"registeration.html",context)

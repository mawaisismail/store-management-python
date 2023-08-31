from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, forms, update_session_auth_hash, decorators
from .forms import UpdateProfileInformation
from .models import UserBilling
from django.db import IntegrityError
from django.core.exceptions import ValidationError


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if confirm_password != password:
            return render(request, "signup.html")
        user = User.objects.filter(username=email).exists()
        if user:
            return render(request, "signup.html")
        new_user = User.objects.create_user(email=email, password=password, username=email, first_name=first_name,
                                            last_name=last_name)
        new_user.save()
        print(new_user)
        return redirect("/user/login")


def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@decorators.login_required(login_url='/user/login/')
def change_password(request):
    print(request.user)
    if request.method == 'POST':
        form = forms.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = forms.PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })


@decorators.login_required(login_url='/user/login/')
def user_profile_view(request):
    if request.method == 'POST':
        form = UpdateProfileInformation(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            area = data['area']
            address = data['address']
            landmark = data['landmark']
            try:
                UserBilling.objects.update_or_create(
                    user_id=request.user.id,
                    defaults={
                        'last_name': last_name,
                        'first_name': first_name,
                        'phone': phone,
                        'area': area,
                        'address': address,
                        'landmark': landmark
                    }
                )
                return render(request, "user-profile-view.html", {"form": form})
            except IntegrityError:
                error_message = "A user billing with similar information already exists."
                return render(request, "user-profile-view.html", {"form": form, "error_message": error_message})
            except ValidationError:
                error_message = "Invalid data provided for user billing."
                return render(request, "user-profile-view.html", {"form": form, "error_message": error_message})

        return render(request, "user-profile-view.html", {"form": form})
    try:
        existing_data = UserBilling.objects.get(user_id=request.user.id)
        initial_data = {
            'first_name': existing_data.first_name,
            'last_name': existing_data.last_name,
            'phone': existing_data.phone,
            'area': existing_data.area,
            'address': existing_data.address,
            'landmark': existing_data.landmark
        }
    except UserBilling.DoesNotExist:
        initial_data = None
    form = UpdateProfileInformation(initial=initial_data)
    return render(request, "user-profile-view.html", {"form": form})

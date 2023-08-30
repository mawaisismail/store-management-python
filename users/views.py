from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, forms, update_session_auth_hash, decorators


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

from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            uname = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=uname).exists():
                messages.error(request, 'username already used')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email aready exists')
                    return redirect('register')
                else:
                    User.objects.create_user(
                        first_name=fname, last_name=lname, username=uname, email=email, password=password)
                    User.save
                    messages.success(
                        request, f"Congratulations {uname}! You have been sucessfully registered!")
                    return redirect('index')
        else:
            messages.error(request, 'Passwords not matching')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome Back {uname}")
            return redirect('index')
        else:
            messages.error(request, 'Sorry, Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You have been successfully logged out")
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

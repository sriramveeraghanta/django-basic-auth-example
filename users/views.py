from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        # print("registration Sccessfull")
        return redirect('/user/login/')
    return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
           # print("login Sucessfull")
            return redirect('/')
        else:
            print("Shit Happened")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/')

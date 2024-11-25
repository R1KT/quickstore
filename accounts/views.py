from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username, password)

        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return render(request, 'login/home.html')
        else:
            messages.error(request, "Login Failed!!")

        return render(request, 'login/login.html')


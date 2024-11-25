from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard_view')
        else:
            messages.error(request, "Login Failed!!")

    return render(request, 'login/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'login/home/html')


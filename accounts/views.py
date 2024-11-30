from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            nextUrl = request.GET.get('next')
            if nextUrl:
                return redirect(nextUrl)
        else:
            messages.error(request, "Login Failed!!")

    return render(request, 'login\login.html')


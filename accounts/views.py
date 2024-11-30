from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def loginView(request):
    if request.method == 'POST':
        print("Form submitted")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            print("User authenticated")
            login(request, user)
            # if 'next' in request.POST:
            #     print(f"Redirecting to: next_url")
            #     return redirect(request.POST['next'])
            # else:
            return redirect('dashboard:home')
        else:
            print("Invalid credentials")
            return render(request, "login/login.html", {'error' : 'Invalid Credentials'})

    return render(request, 'login/login.html')


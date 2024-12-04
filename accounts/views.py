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
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('dashboard:home')
        else:
            return render(request, "login\login.html", {'error' : 'Invalid Credentials'})

    return render(request, 'login\login.html')

def newResidentView(request):
    request.session.set_expiry(0)
    return render(request, 'residents\\newResidents\\newResident.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
def homeView(request):
    request.session.set_expiry(0)
    return render(request, 'home\\home.html')

def residentsView(request):
    request.session.set_expiry(0)
    return render(request, 'residents\\residents.html')

def newResidentView(request):
    request.session.set_expiry(0)
    return render(request, 'residents\\newResident.html')

def servicesView(request):
    request.session.set_expiry(0)
    return render(request, 'services\\services.html')

def guestsView(request):
    request.session.set_expiry(0)
    return render(request, 'guestLog\\guestLog.html')




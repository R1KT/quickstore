from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    request.session.set_expiry(0)
    return render(request, 'home\home.html')




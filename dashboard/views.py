from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    if request.method == 'GET':
        return render(request, 'home\home.html')


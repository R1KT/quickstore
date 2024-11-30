from django.shortcuts import render

def homeView(request):
    if request.method == 'GET':
        return render(request, 'home\home.html')




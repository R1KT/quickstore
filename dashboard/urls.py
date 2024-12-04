from django.urls import path
from .views import *

app_name = "dashboard"

urlpatterns = [
    path('home/', homeView, name='home'),
    path('residents/', residentsView, name='residents'),
    path('residents/new/', residentsView, name='residents'),
    path('services/', servicesView, name='services'),
    path('guests/', guestsView, name='guests'),
]
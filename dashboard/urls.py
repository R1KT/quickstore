from django.urls import path
from .views import *

app_name = "dashboard"

urlpatterns = [
    path('home/', homeView, name='home'),
    path('residents/', residentsView, name='home'),
]
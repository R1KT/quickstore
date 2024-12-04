from django.urls import path
from .views import *


urlpatterns = [
    path('', loginView, name='login'),
    path('/residents/setup/', newResidentView, name='login'),
]
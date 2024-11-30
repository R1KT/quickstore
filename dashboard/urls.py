from django.urls import path
from .views import homeView

app_name = 'dashboard'

urlpatterns = [
    path('home/', homeView, name='home')
]
from django.urls import path
from .views import loginView

app_name = 'accounts'

urlpatterns = [
    path('login/', loginView, name='login'),
]
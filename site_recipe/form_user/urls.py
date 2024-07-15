from django.urls import path

from . import views
from .views import login

urlpatterns = [
    path('login', login, name='login'),
    # path('registration', registration, name='registration'),
]

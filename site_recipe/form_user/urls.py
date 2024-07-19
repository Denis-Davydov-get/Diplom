from django.template.defaulttags import url
from django.urls import path

from . import views
from .views import registrations, login, get_user, add_recipe

urlpatterns = [
    path('login', login, name='login'),
    path('registrations', registrations, name='registrations'),
    path('users/<int:user_id>', get_user, name='users'),
    path('add_recipe', add_recipe, name='add_recipe'),
]

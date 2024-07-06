from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('first_dishes/', views.first_dishes, name='first_dishes'),
    path('second_dishes/', views.second_dishes, name='second_dishes'),
    path('snacks_dishes/', views.snacks_dishes, name='snacks_dishes'),
    path('drink_recipes/', views.drink_recipes, name='drink_recipes'),
    path('sauce_recipes/', views.sauce_recipes, name='sauce_recipes'),
]

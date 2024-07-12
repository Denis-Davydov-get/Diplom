from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('soups_and_broths/', views.soups_and_broths, name='soups_and_broths'),
    path('hot_dishes/', views.hot_dishes, name='hot_dishes'),
    path('salad_recipe/', views.salad_recipes, name='salad_recipe'),
]

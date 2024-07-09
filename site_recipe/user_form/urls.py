from django.urls import path

from . import views

urlpatterns = [
    path('ingredients/', views.add_ingredient, name='add_ingredient'),
    path('add_category/', views.add_category, name='add_category'),
]

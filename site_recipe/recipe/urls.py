from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import index, get_recipe

urlpatterns = [
    path('', index, name='index'),
    path('soups_and_broths/', views.soups_and_broths, name='soups_and_broths'),
    path('hot_dishes/', views.hot_dishes, name='hot_dishes'),
    path('salad_recipe/', views.salad_recipes, name='salad_recipe'),
    path('recipe/<int:recipe_id>/', get_recipe, name='get_recipe'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

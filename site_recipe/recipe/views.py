import logging

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from recipe.models import Category, Recipe

logger = logging.getLogger(__name__)


def index(request):
    logger.info(msg="")
    all_recipe = Recipe.objects.all()
    return render(request,
                  "recipe/index.html",
                  {"title": "Все рецепты",
                   "all_recipe": all_recipe})


def soups_and_broths(request):
    """Рецепты супов и бульонов"""
    logger.info(msg="Рецепты супов и бульонов")
    all_recipe_soups_and_broths = Recipe.objects.filter(categories=1)
    return render(request,
                  "recipe/soups_and_broths.html",
                  {"title": "Рецепты супов и бульонов",
                   "all_recipe_soups_and_broths": all_recipe_soups_and_broths})


def hot_dishes(request):
    """Рецепты горячих блюд"""
    logger.info(msg="Рецепты горячих блюд")
    all_recipe_hot_dishes = Recipe.objects.filter(categories=2)
    return render(request,
                  "recipe/hot_dishes.html",
                  {"title": "Рецепты горячих блюд",
                   "all_recipe_hot_dishes": all_recipe_hot_dishes})


def salad_recipes(request):
    """Рецепты салатов"""
    logger.info(msg="Рецепты салатов")
    all_recipe_salad_recipes = Recipe.objects.filter(categories=3)
    return render(request,
                  "recipe/salad_recipe.html",
                  {"title": "Рецепты салатов",
                   "all_recipe_salad_recipes": all_recipe_salad_recipes})


def get_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    logger.info(msg=f"Запрошен рецепт {recipe.title}")
    recipe.views += 1
    recipe.save()
    return render(request,
                  "recipe/recipe.html",
                  {"recipe": recipe})



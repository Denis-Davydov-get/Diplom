import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info(msg="")
    return render(request, "recipe/index.html", {"title": "Homepage"})


def first_dishes(request):
    """Рецепты первых блюд"""
    logger.info(msg="")
    return render(request,
                  "recipe/first_dishes.html",
                  {"title": "Рецепты первых блюд"})


def second_dishes(request):
    """Рецепты вторых блюд"""
    logger.info(msg="")
    return render(request,
                  "recipe/second_dishes.html",
                  {"title": "Рецепты вторых блюд"})


def snacks_dishes(request):
    """Рецепты закусок"""
    logger.info(msg="")
    return render(request,
                  "recipe/snacks_dishes.html",
                  {"title": "Рецепты закусок"})


def drink_recipes(request):
    """Рецепты напитков"""
    logger.info(msg="")
    return render(request,
                  "recipe/drink_recipes.html",
                  {"title": "Рецепты напитков"})


def sauce_recipes(request):
    """Рецепты соусов"""
    logger.info(msg="")
    return render(request,
                  "recipe/sauce_recipes.html",
                  {"title": "Рецепты соусов"})

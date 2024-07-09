import logging
from recipe.models import Ingredients, Category, Recipe, User
from django.shortcuts import render
from .forms import IngredientsForm, CategoryForm

logger = logging.getLogger(__name__)


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientsForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            ingredient = Ingredients(name=name)
            ingredient.save()
            message = 'Ингридиент сохранён'

    else:
        form = IngredientsForm()
        message = 'Заполните форму'
    return render(request,
                  'user_form/ingredients_form.html',
                  {'form': form, 'message': message})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            category = Category(name=name)
            category.save()
            message = 'Категория сохранёна'

    else:
        form = CategoryForm()
        message = 'Заполните форму'
    return render(request,
                  'user_form/category_form.html',
                  {'form': form, 'message': message})


def add_recipe(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            categories = form.cleaned_data['categories']
            photo = form.cleaned_data['photo']
            author = form.cleaned_data['author']
            recipe = Recipe(title=title,
                            description=description,
                            ingredients=ingredients,
                            categories=categories,
                            photo=photo,
                            author=author)
            recipe.save()
            message = 'Рецепт сохранён'

    else:
        form = CategoryForm()
        message = 'Заполните форму'
    return render(request,
                  'user_form/category_form.html',
                  {'form': form, 'message': message})




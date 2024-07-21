from django.shortcuts import render, get_object_or_404
from recipe.form import UserRegistrationForm, UserLoginForm
from recipe.models import User, Recipe

from .forms import NewRecipe


def registrations(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = User(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"], )
            new_user.save()
            return redirect(login)
    else:
        form = UserRegistrationForm()
    return render(request,
                  "form_user/registrations.html",
                  {"title": "Логин",
                   "form": form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            new_user = User(
                name=form.cleaned_data["name"],
                password=form.cleaned_data["password"], )
            new_user.save()
            return redirect(login)
    else:
        form = UserLoginForm()
    return render(request,
                  "form_user/login.html",
                  {"title": "Логин",
                   "form": form})


def logout_view(request):
    logout(request)
    return


def get_user(request, user_id):
    user_info = get_object_or_404(User, pk=user_id)
    logger.info(msg=f"{User.name}")
    return render(request,
                  "form_user/user.html",
                  {"user_info": user_info})


def add_recipe(request):
    if request.method == "POST":
        form_new_ricipe = NewRecipe(request.POST)
        if form_new_ricipe.is_valid():
            new_recipe = Recipe(
                title=form_new_ricipe.cleaned_data["title"],
                description=form_new_ricipe.cleaned_data["description"],
                ingredients_name=form_new_ricipe.cleaned_data["ingredients_name"],
                ingredients_quantity=form_new_ricipe.cleaned_data["ingredients_quantity"],
                categories=form_new_ricipe.cleaned_data["categories"],
                photo=form_new_ricipe.cleaned_data["photo"])
            new_recipe.save()
            return redirect(add_recipe)
    else:
        form_new_ricipe = NewRecipe()
    return render(request,
                  "form_user/add_recipe.html",
                  {"title": "Добавить новый рецепт",
                   "form": form_new_ricipe})

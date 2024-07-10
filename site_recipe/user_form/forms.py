from django import forms
from django.contrib.auth import get_user_model
from recipe.models import Ingredients, Category


class IngredientsForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите название ингридиента'}))


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите название категории'}))


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Введите название рецепта'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите описание рецепта'}))

    ingredients = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Ingredients.objects.all()

    )
    categories = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[', '.join([category.name for category in Category.objects.all()])]
    )
    photo = forms.ImageField()
    author = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=get_user_model(),
    )




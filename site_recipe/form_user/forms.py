from datetime import datetime

from django import forms

from recipe.models import Recipe

from recipe.models import Category, Ingredients


class NewRecipe(forms.Form):
    title = forms.CharField(label="Название рецепта")
    description = forms.Textarea()
    ingredients = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Ingredients.objects.all())
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    photo = forms.ImageField()
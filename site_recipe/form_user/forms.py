from django import forms

from recipe.models import Category, Recipe, Ingredients


class NewRecipe(forms.Form):
    title = forms.CharField(label="Название рецепта")
    description = forms.Textarea()
    ingredients_name = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                      queryset=Ingredients.objects.values('name', "quantity"))
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                queryset=Category.objects.values('name'))
    photo = forms.ImageField()


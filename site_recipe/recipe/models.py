from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return (f'Название категории - {self.name},'
                f'дата добавления - {self.date_added}')


class Ingredients(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Название игридиента - {self.name},'
                f'дата добавления - {self.date_added}')


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    categories = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to='media/', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='recipes', null=True,
                               default=None)
    views = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Название рецепта {self.title}, "
                f"описание - {self.description},"
                f"ингридиенты - {self.ingredients},"
                f"категория - {self.categories},"
                f"автор - {self.author},"
                f"дата обновления - {self.date_updated}")

    class Meta:
        ordering = ('-views',)

    def display_categories(self):
        return ', '.join([category.name for category in self.categories.all()])

    display_categories.short_description = 'Категории рецептов'

    def display_ingredients(self):
        return ', '.join([ingredient.name for ingredient in self.ingredients.all()])

    display_ingredients.short_description = 'Ингридиенты'

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Category(models.Model):
    """Класс для создания модели категория рецепта."""
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return (f'Название категории - {self.name},'
                f'дата добавления - {self.date_added}')


class Ingredients(models.Model):
    """Класс для создания модели ингридиент."""
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Название игридиента - {self.name},'
                f'дата добавления - {self.date_added}')


class Recipe(models.Model):
    """Класс для создания модели рецепт."""
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
        """Функция для вывода всех категорий."""
        return ', '.join([category.name for category in self.categories.all()])

    display_categories.short_description = 'Категории рецептов'

    def display_ingredients(self):
        """Функция для вывода всех ингридиентов."""
        return ', '.join([ingredient.name for ingredient in self.ingredients.all()])

    display_ingredients.short_description = 'Ингридиенты'


class User(models.Model):
    """Класс для создания модели пользователь."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)



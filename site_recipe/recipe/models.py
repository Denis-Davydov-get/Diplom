from django.db import models


class Recipe(models.Model):
    title = models.ExpressionList("Название ингридиента", max_length=50)
    ingredients = models.TextField("Описание рецепта")

    def __str__(self):
        return (f"Название рецепта {self.title}, "
                f"ингридиенты рецепта {self.ingredients}")

from django.contrib import admin

from recipe.models import Category, Ingredients, Recipe, User


@admin.action(description="Сбросить количество в ноль")


def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added']
    list_filter = ['name', "date_added"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title',
                    "views",
                    "date_added",
                    "date_updated"
                    ]
    ordering = ['date_added', '-date_updated']
    list_filter = ['title', 'views', "date_added", "date_updated"]


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added', "quantity"]
    list_filter = ['name', "date_added", "quantity"]
    actions = [reset_quantity]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User)

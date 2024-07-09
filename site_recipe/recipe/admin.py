from django.contrib import admin

from recipe.models import Category, Ingredients, Recipe, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added']
    list_filter = ['name', "date_added"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    "views",
                    "date_added",
                    "date_updated"
                    ]
    ordering = ['date_added', '-date_updated']
    list_filter = ['title', 'views', "date_added", "date_updated"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredients)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User)

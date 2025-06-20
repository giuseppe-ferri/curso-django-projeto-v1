from django.contrib import admin
from .models import Category, Recipe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Category, CategoryAdmin)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

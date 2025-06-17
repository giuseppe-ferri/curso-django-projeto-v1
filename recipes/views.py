from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
# Django reconize the templates folders and search the HTML into it
# Add name spacing "recipes" into the templates folder to avoid name colision

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
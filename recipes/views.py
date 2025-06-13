from django.shortcuts import render

# Create your views here.
# Django reconize the templates folders and search the HTML into it
# Add name spacing "recipes" into the templates folder to avoid name colision

def home(request):
    return render(request, 'recipes/pages/home.html')

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): # mostra o nome da categoria ao usar o admin
        return self.name

class Recipe(models.Model): # class = table
    title = models.CharField(max_length=100) # varchar(100)
    description = models.CharField(max_length=200)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=100)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=100)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # No momento da criação registra a data, a data é fixada
    updated_at = models.DateTimeField(auto_now=True) # Registra a data quando há alguma alteração no registro
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None) # Se o registro n conter Category, fica null
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    def __str__(self):
        return self.title


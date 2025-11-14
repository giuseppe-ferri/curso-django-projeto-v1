
from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip

# "resolve" is used to read a URL and determine the corresponding view.
# "reverse" can generate a URL string using the data defined in url.py, such as 
# the namespace and the view name.

class RecipeViewsTest(RecipeTestBase):
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home')) # '/'
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    @skip('WIP') # [W]ork [I]n [P]rogress -> This test will be skipped
    def test_recipe_home_template_shows_no_recipes_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))
        
        # Reminder to create more tests
        self.fail('You must create more tests')

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()
        # Check if the page is loading
        response = self.client.get(reverse('recipes:home'))
        # Check if the content of the page is being shown on the screen
        content = response.content.decode('utf-8')
        # Shows the recipe
        response_context_recipes = response.context['recipes']
        # Verify if string is in the content -> Check if one recipe exists
        self.assertIn('Recipe Title', content)
        # Check if one recipe was created
        self.assertEqual(len(response_context_recipes), 1)
        
    def test_recipe_home_template_dont_load_recipes_not_publisehd(self):
        '''Test that a recipe with is_published set to False is not displayed'''
        # Need a recipe for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        
        # Check if one recipe exists
        self.assertIn(
            'No recipes found', 
            response.content.decode('utf-8')
        )
        
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        
        # Check if one recipe exists
        self.assertIn(needed_title, content)
        
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        '''Test that a recipe is_published set to False is not displayed'''
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={
            'id': recipe.id, # id: 1
        }))
        self.assertEqual(response.status_code, 404)
        print(f'id: {recipe.id}')

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1})) # '/'
        self.assertIs(view.func, views.category)

    def test_recipes_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1})) # '/'
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        print(f'status code: {response.status_code}')
        
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'
        
        # Need a recipe for this test
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        
        # Check if one recipe exists
        self.assertIn(needed_title, content)
        
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        '''Test that a recipe is_puslished set to False is not displayed'''
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={
            'id': recipe.id,
        }))
        
        self.assertEqual(response.status_code, 404)
        print(f'status code: {response.status_code}\nid: {recipe.id}')
        
    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)
from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name=models.TextField(max_length=100)
    recipe_discription=models.TextField()
    recipe_image=models.ImageField(upload_to='recipe/' )
from django.shortcuts import render,redirect
from .models import *

def recipe(request):
    if request.method=='POST':
        data=request.POST
        
        recipe_image=request.FILES.get('recipe_image')
        
        recipe_name=data.get('recipe_name')
        recipe_discription=data.get('recipe_discription')
        
        Recipes.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_discription=recipe_discription,
        )
        
    
        return redirect('/recipe/')
    
    queryset=Recipes.objects.all()
    context={'recipe':queryset}
        
    return render(request,'recipe.html',context)

def delete_item(request, id):
    query=Recipes.objects.get(id = id)
    query.delete()
    return redirect('/recipe/')
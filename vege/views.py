from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
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
    if request.GET.get('search'):
         queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
        
    context={'recipe':queryset}
    
    
        
    return render(request,'recipe.html',context)

def delete_item(request, id):
    queryset=Recipes.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')


def update_item(request, id):
    queryset=Recipes.objects.get(id = id)
    
    if request.method=="POST":
        data=request.POST
        
         
        recipe_image=request.FILES.get('recipe_image')
        
        recipe_name=data.get('recipe_name')
        recipe_discription=data.get('recipe_discription')
    
        queryset.recipe_name=recipe_name
        queryset.recipe_discription=recipe_discription
        
        if recipe_image:
         queryset.recipe_image=recipe_image
        
        queryset.save()
        return redirect('/recipe/')
        
    
    context={'recipe':queryset}
    return render(request,'update.html',context)
    
    
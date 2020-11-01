from django.shortcuts import render, redirect
from main_app.models import Recipe
from main_app.forms import RecipeForm, DeleteRecipeForm


# Create your views here.
def index(request):
    # recipes = Recipe.objects.order_by('id')
    recipes = Recipe.objects.all()
    context = {
        'form': RecipeForm(),
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'delete.html', context)
    recipe.delete()
    return redirect('index')


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(", ")
    }
    return render(request, 'details.html', context)

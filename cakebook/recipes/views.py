from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import CakeRecipe
from .forms import CakeRecipeForm
from django.contrib.auth.decorators import login_required

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = CakeRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, "🎂 Recipe added successfully!")
            return redirect('home')
    else:
        form = CakeRecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


# Home Page
def home(request):
    recipes = CakeRecipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

# Recipe Detail Page
def recipe_detail(request, pk):
    recipe = get_object_or_404(CakeRecipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "🎉 Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "❌ Registration failed. Please correct the errors.")
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"🍰 Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "❌ Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "👋 You’ve been logged out.")
    return redirect('home')

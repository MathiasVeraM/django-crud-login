from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from django.contrib import messages

# Create your views here.
def validate_login(request):
    if request.user.is_authenticated:
        return redirect("profile")

def register_view(request):
    validate_login(request)  # si ya está logueado, va al perfil

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente. Ahora inicia sesión.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "account/register.html", {"form": form})

def login_view(request):
    validate_login(request)  # si ya está logueado, va al perfil

    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, "account/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    return render(request, "account/profile.html", {"user": request.user})

@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, "account/edit_profile.html", {"form": form})

@login_required
def erase_account_view(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Cuenta eliminada correctamente.")
        return redirect("login")
    return render(request, "account/erase_account.html")
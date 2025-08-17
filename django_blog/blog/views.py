from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
    ProfileUpdateForm,
)

# 👤 Registration

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            messages.success(request, "Your account was created successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# 📝 Profile (view + edit)

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors and try again.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "blog/profile.html", context)

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from workers.models import WorkerProfile
from .forms import UserRegisterForm, UserLoginForm
from .models import Profile

# ---------- LOGIN + REGISTER COMBINED ----------
def login_page(request):
    login_form = UserLoginForm(request, data=request.POST or None)
    register_form = UserRegisterForm(request.POST or None)

    # If user clicks Login
    if "login_submit" in request.POST:
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            # Redirect by role
            if hasattr(user, "profile"):
                if user.profile.role == "customer":
                    return redirect("customer_dashboard")
                elif user.profile.role == "worker":
                    return redirect("worker_dashboard")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    # If user clicks Register
    elif "register_submit" in request.POST:
        if register_form.is_valid():
            user = register_form.save()
            role = register_form.cleaned_data.get("role")
            Profile.objects.create(user=user, role=role)

            if role == "worker":
                WorkerProfile.objects.create(user=user)

            messages.success(request, f"{role.capitalize()} account created successfully! Please login.")
            return redirect("login_page")
        else:
            messages.error(request, "Registration failed. Please check the form.")

    return render(request, "login.html", {
        "login_form": login_form,
        "register_form": register_form,
    })


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    return redirect("home")

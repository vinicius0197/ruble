from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, SignupForm

def index(request):
    """ Renders main landing page """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_view"))
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    """ Renders login view """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "users/login.html", {"message": "Invalid credentials."})
    else:
        form = LoginForm()

    context = {
        "message": None,
        "form": form
    }

    return render(request, "users/login.html", context)

def logout_view(request):
    """ Logout the user """
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def signup(request):
    """ Register a new user """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email, password)
            user.save()

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/signup.html")
    else:
        form = SignupForm()

    context = {
        "form": form
    }
    return render(request, "users/signup.html", context)
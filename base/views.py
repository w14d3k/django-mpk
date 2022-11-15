from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
from django. contrib import messages
from .forms import LoginForm, RegisterForm, User


def home(request):
    return render(request, 'base/home.html')

User = get_user_model()

def register_user(request):
    if request.method == 'POST':
         form = RegisterForm(request.POST or None)
         if form.is_valid():
             form.save()
    else:
        form = RegisterForm()     
    return render(request, 'base/register.html', context = {"form" : form})

def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print("Error")
    return render(request, "base/login.html", context)

def profile(request):
    return render(request, 'base/profile.html')
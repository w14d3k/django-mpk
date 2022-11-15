from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django. contrib import messages
from .forms import LoginForm, RegisterForm, User


def home(request):
    return render(request, 'base/home.html')

User = get_user_model()

def register_user(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')  
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
            return redirect('/store')
        else:
            print("Error")
    return render(request, "base/login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'base/profile.html')

def price_list(request):
    return render(request, 'base/price_list.html')

def store(request):
    return render(request, 'base/store.html')

def contact(request):
    return render(request, 'base/contact.html')

def terms(request):
    return render(request, 'base/terms.html')

def gdpr(request):
    return render(request, 'base/gdpr.html')

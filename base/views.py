from django.contrib.auth import authenticate, get_user_model, login
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def registration(request):
    return render(request, 'base/register.html')

def login(request):
    return render(request, 'base/login.html')

def profile(request):
    return render(request, 'base/profile.html')
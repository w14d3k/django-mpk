from django.contrib import messages
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import TicketsList, UserPurchasediTcketsList


def home(request):
    return render(request, 'base/home.html')

User = get_user_model()

def register_user(request):
    registration_form = RegisterForm(request.POST)
    context = {
        "registration_form": registration_form
    }
    if request.method == 'POST':
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            registration_form = RegisterForm()  
            return redirect('/profile')
        registration_form = RegisterForm()
    return render(request, 'base/register.html', context)


def login_user(request):
    login_form = LoginForm(request.POST)
    context = {
        "login_form": login_form
    }
    if request.method == 'POST':
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        login_form = LoginForm()    
    return render(request, "base/login.html", context)


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def profile(request):
    return render(request, 'base/profile.html')


@login_required(login_url='/')
def settings(request):
   return render(request, 'base/settings.html') 


def admin_dashboard(request):
    return redirect('/admin')


def sales_statistics(request):
    return redirect('/admin')


def price_list(request):
    tickets_list = TicketsList.objects.all()
    context = {
        "tickets_list": tickets_list,
    }
    return render(request, 'base/price_list.html', context)


@login_required(login_url='/')
def store(request):
    tickets_list = TicketsList.objects.all()
    context = {
        "tickets_list": tickets_list,
    }
    return render(request, 'base/store.html', context)


def contact(request):
    return render(request, 'base/contact.html')


def terms(request):
    return render(request, 'base/terms.html')


def gdpr(request):
    return render(request, 'base/gdpr.html')


def about_us(request):
    return render(request, 'base/about_us.html')


def careers(request):
    return render(request, 'base/careers.html')


def media(request):
    return render(request, 'base/media.html')

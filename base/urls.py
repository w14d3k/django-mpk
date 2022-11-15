from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.register_user, name="registration"),
    path('login/', views.login_user, name="login"),
    path('profile/', views.profile, name="profile"),
]

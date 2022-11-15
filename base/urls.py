from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.register_user, name="registration"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('price_list/', views.price_list, name="price_list"),
    path('store/', views.store, name="store"),
    path('terms/', views.terms, name="terms"),
    path('gdpr/', views.gdpr, name="gdpr"),
    path('contact/', views.contact, name="contact"),
]

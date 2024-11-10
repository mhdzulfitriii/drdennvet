from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('doctor.html', views.doctor, name="doctor"),
    path('pricing.html', views.pricing, name="pricing"),
    path('department.html', views.department, name="department"),
    path('main.html', views.department, name="main"),
    path('index.html', views.home, name='home'),
    path('login.html', login_view, name='login'),
    path('loginAdmin.html', views.loginAdmin, name='loginAdmin'),
    path('loginEmploy.html', views.loginEmploy, name='loginEmploy'),
    path('dashboard.html', views.dashboard, name='dashboard'),
]








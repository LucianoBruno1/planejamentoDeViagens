from django.urls import path
from . import views
from .views import register, CustomLoginView, profile
from django.contrib.auth import views as auth_views
from .views import about


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('about/', about, name='about')
]

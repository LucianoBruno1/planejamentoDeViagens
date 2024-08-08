from django.urls import path
from . import views
from .views import register, CustomLoginView, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
]

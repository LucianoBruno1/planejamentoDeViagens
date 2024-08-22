from django.urls import path
from . import views

urlpatterns = [
    path('prices/', views.get_flights, name='get_flights'),
]

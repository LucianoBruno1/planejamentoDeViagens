from django.urls import path
from .views import destination_list

urlpatterns = [
    path('', destination_list, name='destination_list'),
]

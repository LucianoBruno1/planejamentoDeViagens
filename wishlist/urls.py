from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:destination_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('', views.wishlist_view, name='wishlist_view'),
    path('remove/<int:destination_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),  # Certifique-se de que esta linha existe


]

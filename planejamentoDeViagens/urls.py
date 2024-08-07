# planejamentoDeViagens/urls.py

from django.contrib import admin
from django.urls import path, include
from planejamentoDeViagens.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', home, name='home'),
]

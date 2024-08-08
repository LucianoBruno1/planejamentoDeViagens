# planejamentoDeViagens/urls.py

from django.contrib import admin
from django.urls import path, include
from planejamentoDeViagens.views import home
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', home, name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

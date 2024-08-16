# planejamentoDeViagens/urls.py

from django.contrib import admin
from django.urls import path, include
from planejamentoDeViagens.views import home
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', home, name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('destinations/', include('destinations.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

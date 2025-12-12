# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings
from django.conf.urls.static import static # Importa static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Le decimos a Django que para cualquier URL que empiece con 'accounts/',
    # use las URLs pre-construidas que él ofrece.
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('condominio.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
URL configuration for CryptoMohem project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints will be added in later phases
    # path('api/', include('apps.news.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "CryptoMohem Administration"
admin.site.site_title = "CryptoMohem Admin"
admin.site.index_title = "Welcome to CryptoMohem Administration"

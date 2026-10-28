from django.contrib import admin
from django.urls import path, include

# Импорты для медиа-файлов (ТОЛЬКО ЗДЕСЬ, не в products/urls.py!)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем приложение products
    path('products/', include('products.urls')),
]

# Добавляем медиа-файлы ТОЛЬКО если DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

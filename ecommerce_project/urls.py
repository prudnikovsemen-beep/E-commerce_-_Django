from django.contrib import admin
from django.urls import path, include

# Импорты для медиа-файлов (ставь их в самом верху, вместе с другими импортами)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем пути из приложения products
    path('products/', include('products.urls')),
]

# Добавляем поддержку медиа-файлов ТОЛЬКО если режим DEBUG включен
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

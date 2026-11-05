from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", "catalog")),
    path("blogs/", include("blog.urls", "blog")),
=======
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
>>>>>>> 7591698f110accc0bc3bffa9c18ba7708eb6859e
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

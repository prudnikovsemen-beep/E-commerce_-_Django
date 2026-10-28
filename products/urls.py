from django.urls import path
from . import views  # Импортируем функции из файла views.py, который лежит в этой же папке

app_name = 'products'  # Это пространство имен. Оно нужно, чтобы Django понимал, к какому приложению относятся ссылки

urlpatterns = [
    # Главная страница списка товаров (например, /products/)
    path('', views.product_list, name='product_list'),

    # Страница конкретного товара (например, /products/5/)
    # <int:pk> означает, что Django ждет число (id товара) в адресе
    path('<int:pk>/', views.product_detail, name='product_detail'),

    # Страница добавления товара (например, /products/add/)
    path('add/', views.add_product, name='add_product'),
]

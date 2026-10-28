from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # Если позже добавишь детали товара, раскомментируй строку ниже:
    path('<int:pk>/', views.product_detail, name='product_detail'),
]

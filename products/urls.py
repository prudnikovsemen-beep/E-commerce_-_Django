from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # Критерий: URL вида /products/int:pk/, нейминг product_detail
    path('<int:pk>/', views.product_detail, name='product_detail'),
]

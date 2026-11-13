from django.urls import path

from catalog import views
from catalog.views import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, ContactsView, AllProductsView,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/", views.catalog_view, name="catalog"),
    path("category/<int:pk>/", views.category_detail_view, name="category_detail"),
    path("all/", AllProductsView.as_view(), name="all_products"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Product, ContactInfo
from blog.models import Blog


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "latest_products"

    def get_queryset(self):
        # Только товары в продаже, последние 5
        return Product.objects.filter(is_active=True).order_by("-created_at")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Последние 3 опубликованные статьи блога для главной
        context["latest_articles"] = Blog.objects.filter(is_published=True).order_by("-created_at")[:3]
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price", "image")
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "image")
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Берём единственную запись с контактами (или None, если ещё не создана)
        context["contact"] = ContactInfo.objects.first()
        return context

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Product, ContactInfo


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"  # или твой шаблон списка, если он другой
    context_object_name = "latest_products"

    def get_queryset(self):
        # Получаем последние 5 созданных продуктов (по полю created_at)
        queryset = Product.objects.order_by("-created_at")[:5]

        # Вывод в консоль сервера (видно в терминале с runserver)
        print("=== Последние 5 продуктов на главной ===")
        for product in queryset:
            print(f"- {product.name} (цена: {product.price}, создан: {product.created_at})")
        print("==========================================")

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price")  # подставь свои поля модели
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price")
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

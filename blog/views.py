import re

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings

from blog.models import Blog, BlogSettings

from catalog.models import Product  # если модель товаров называется иначе — поправьте


def home(request):
    latest_articles = Blog.objects.filter(is_published=True).order_by('-created_at')[:3]
    latest_products = Product.objects.all()[:4]
    return render(request, 'blog/home.html', {
        'latest_articles': latest_articles,
        'latest_products': latest_products,
    })


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        # выводим только опубликованные статьи
        return Blog.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # настройки приветствия (модель BlogSettings, редактируются в админке)
        context["settings"] = BlogSettings.objects.first()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # увеличиваем счётчик просмотров при открытии статьи
        obj.views_count += 1
        obj.save(update_fields=["views_count"])
        self._congratulate_if_needed(obj)
        return obj

    def _find_related_products(self, title):
        """Ищем товары по словам из заголовка статьи."""
        # слова от 4 букв — предлоги и союзы пропускаем
        words = re.findall(r"[а-яёА-ЯЁa-zA-Z]{4,}", title)
        matched_ids = set()
        for word in words:
            hits = Product.objects.filter(name__icontains=word)
            matched_ids.update(hits.values_list("pk", flat=True))
        return Product.objects.filter(pk__in=matched_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # автоматический подбор товаров по заголовку статьи
        found = self._find_related_products(self.object.title)
        # в наличии = остаток на складе больше 0 и товар в продаже
        in_stock = found.filter(stock__gt=0, is_active=True)[:6]

        context["products_carousel"] = in_stock
        # карусель показываем только если нашлись товары в наличии
        context["show_carousel"] = in_stock.exists()
        return context

    def _congratulate_if_needed(self, obj):
        if obj.views_count == 100:
            send_mail(
                subject="Поздравляем с достижением!",
                message=f'Статья «{obj.title}» набрала 100 просмотров!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published")
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published")
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        # после редактирования ведём пользователя на отредактированную статью
        return reverse_lazy("blog:blog_detail", args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")

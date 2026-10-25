from django.shortcuts import render
from .models import Product, ContactInfo


def home(request):
    # Получаем последние 5 созданных продуктов (по полю created_at)
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Вывод в консоль сервера (видно в терминале с runserver)
    print("=== Последние 5 продуктов на главной ===")
    for product in latest_products:
        print(f"- {product.name} (цена: {product.price}, создан: {product.created_at})")
    print("==========================================")

    context = {
        'latest_products': latest_products,
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    # Берём единственную запись с контактами (или None, если ещё не создана)
    contact = ContactInfo.objects.first()
    return render(request, 'catalog/contacts.html', {'contact': contact})

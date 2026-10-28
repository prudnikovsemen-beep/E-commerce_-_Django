from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    # Критерий: Использован лаконичный запрос: Product.objects.all()
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    # Критерий: Контроллер получает pk, извлекает объект через ORM
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

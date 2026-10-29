from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator  # Если нужна пагинация


def product_list(request):
    products = Product.objects.all()
    # Если нужно выполнить доп. задание по пагинации, раскомментируй строки ниже:
    # paginator = Paginator(products, 10)
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)

    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    # Критерий: Контроллер получает pk, извлекает объект через ORM
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

from django.shortcuts import render

def product_list(request):
    # Передаем пустой список, чтобы шаблон не ругался, если товаров пока нет
    context = {
        'products': [
            {'name': 'Смартфон X', 'price': 25000},
            {'name': 'Наушники Y', 'price': 5000},
        ]
    }
    return render(request, 'products/product_list.html', context)

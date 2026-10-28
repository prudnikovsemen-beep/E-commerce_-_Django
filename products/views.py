from django.shortcuts import render

def product_list(request):
    # Пока просто возвращаем простой текст, чтобы проверить, что пути работают
    return render(request, 'products/product_list.html', {'products': })

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'image']
        # Если в твоей модели Product есть ещё обязательные поля (например, category),
        # добавь их в список через запятую: ['name', 'category', 'description', 'price', 'image']

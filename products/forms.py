import re  # ← добавить

from django import forms

from .models import Product

FORBIDDEN_WORDS = [  # ← добавить
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


def validate_no_forbidden_words(value: str):  # ← добавить
    lowered = value.lower()
    for word in FORBIDDEN_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            raise forms.ValidationError(
                f'Слово «{word}» запрещено в названии и описании продукта.'
            )



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'image']
        # Если в твоей модели Product есть ещё обязательные поля (например, category),
        # добавь их в список через запятую: ['name', 'category', 'description', 'price', 'image']

    def clean_name(self):  # ← добавить
        name = self.cleaned_data['name']
        validate_no_forbidden_words(name)
        return name

    def clean_description(self):  # ← добавить
        description = self.cleaned_data['description']
        validate_no_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price
import re

from django import forms

from .models import Product

FORBIDDEN_WORDS = [
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


def validate_no_forbidden_words(value: str):
    lowered = value.lower()
    for word in FORBIDDEN_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            raise forms.ValidationError(
                f'Слово «{word}» запрещено в названии и описании продукта.'
            )


class StyleFormMixin:
    """Единая стилизация полей под общую стилистику платформы."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Точечная стилизация отдельных полей
        self.fields["name"].widget.attrs["placeholder"] = "Введите название продукта"
        self.fields["price"].widget.attrs.update({
            "placeholder": "Укажите цену",
            "step": "0.01",
        })
        self.fields["description"].widget.attrs["rows"] = 4

    def clean_name(self):
        name = self.cleaned_data["name"]
        validate_no_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        validate_no_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

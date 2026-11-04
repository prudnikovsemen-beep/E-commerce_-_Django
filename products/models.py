from django.db import models

class Category(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Изображение", upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", null=True, blank=True)

    def __str__(self):
        return self.name

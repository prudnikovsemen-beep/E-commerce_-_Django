from django.contrib import admin
from .models import Category, Product, ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
    fieldsets = (
        ("Контакты", {
            "fields": ('phone', 'email', 'telegram', 'whatsapp'),
        }),
        ("Адрес и время работы", {
            "fields": ('address', 'working_hours'),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}  # если у тебя есть slug — оставь, если нет — удали эту строку

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

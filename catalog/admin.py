from django.contrib import admin

from .models import Category, Product, ContactInfo, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = (ProductImageInline,)

    fieldsets = (
        (None, {
            "fields": ("category", "name", "slug", "description"),
        }),
        ("Цена и наличие", {
            "fields": ("price", "stock", "is_active"),
        }),
        ("Основное фото", {
            "fields": ("image",),
        }),
        ("Служебные данные", {
            "classes": ("collapse",),   # блок свёрнут по умолчанию
            "fields": ("created_at", "updated_at"),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


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

from .models import Blog, BlogSettings
from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count")
    list_display_links = ("id", "title")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)


@admin.register(BlogSettings)
class BlogSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'subtitle'),
        }),
    )
    # Запрещаем удаление, чтобы случайно не стереть настройки
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

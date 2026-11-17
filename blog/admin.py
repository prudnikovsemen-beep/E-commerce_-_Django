from django.contrib import admin

from .models import Blog, BlogSettings


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "created_at", "is_published", "views_count")
    list_display_links = ("id", "title")
    list_filter = ("is_published", "type", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)

    fieldsets = (
        ("Основное", {
            "fields": ("title", "type", "preview", "is_published"),
        }),
        ("Текст статьи", {
            "fields": ("content",),
            "description": "Заполняется для статей. Для видео-публикации — это описание к ролику.",
        }),
        ("Видео", {
            "fields": ("video_url",),
            "description": "Только для типа «Видео». Вставляйте embed-ссылку с хостинга (VK, RuTube, YouTube), например https://rutube.ru/play/embed/...",
        }),
    )


@admin.register(BlogSettings)
class BlogSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Основное", {
            "fields": ("title", "subtitle"),
        }),
    )
    # Запрещаем удаление, чтобы случайно не стереть настройки
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

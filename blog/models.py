from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Blog(models.Model):
    TYPE_CHOICES = (
        ("article", "Статья"),
        ("video", "Видео"),
    )

    title = models.CharField(max_length=150, verbose_name="заголовок")
    content = CKEditor5Field(verbose_name="содержимое", config_name="default")
    preview = models.ImageField(upload_to="blog/previews/", verbose_name="превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")
    type = models.CharField(
        "тип публикации",
        max_length=10,
        choices=TYPE_CHOICES,
        default="article",
    )

    # Поле для видео-публикаций
    video_url = models.URLField(
        "ссылка на видео (VK, RuTube, YouTube)",
        blank=True,
        help_text="Вставляйте embed-ссылку, например https://rutube.ru/play/embed/..."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блоговая запись"
        verbose_name_plural = "блоговые записи"

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.pk])


class BlogSettings(models.Model):
    """
    Настройки блога. Создаётся 1 раз в админке.
    Поля можно менять через админку без правки HTML.
    """
    title = models.CharField(max_length=200, verbose_name="Заголовок приветствия", default="Раздел Блога")
    subtitle = models.TextField(verbose_name="Подзаголовок / описание",
                                default="Здесь мы публикуем статьи о камнях, огранке и новостях проекта Skystore.")

    class Meta:
        verbose_name = "Настройки блога"
        verbose_name_plural = "Настройки блога"

    def __str__(self):
        return "Настройки блога"

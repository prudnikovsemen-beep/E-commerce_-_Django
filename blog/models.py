from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    content = CKEditor5Field(verbose_name="содержимое", config_name="default")
    preview = models.ImageField(upload_to="blog/previews/", verbose_name="превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блоговая запись"
        verbose_name_plural = "блоговые записи"

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.pk])


# users/models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар"
    )
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон"
    )
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Страна"
    )
    nickname = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Ник",
        help_text="Отображаемое имя пользователя",
    )
    patronymic = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Отчество"
    )

    DELIVERY_POINTS = [
        ("tlt_center", "Тольятти, ул. Центральная, 1"),
        ("tlt_south", "Тольятти, ул. Южная, 15"),
        ("samara", "Самара, ул. Полевая, 7"),
    ]
    delivery_point = models.CharField(
        max_length=50,
        choices=DELIVERY_POINTS,
        blank=True, null=True,
        verbose_name="Пункт выдачи заказов",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

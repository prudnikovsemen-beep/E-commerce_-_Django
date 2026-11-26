# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["type"] = "email"
        self.fields["username"].label = "Email"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "avatar",
            "nickname",
            "last_name",
            "first_name",
            "patronymic",
            "email",
            "phone",
            "country",
            "delivery_point",
        )
        labels = {
            "avatar": "Аватар",
            "nickname": "Ник",
            "last_name": "Фамилия",
            "first_name": "Имя",
            "patronymic": "Отчество",
            "email": "Email",
            "phone": "Телефон",
            "country": "Страна",
            "delivery_point": "Пункт выдачи заказов",
        }
        widgets = {
            "nickname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ник",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите фамилию",
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя",
            }),
            "patronymic": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите отчество",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Введите email",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите телефон",
            }),
            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите страну",
            }),
            "delivery_point": forms.Select(attrs={
                "class": "form-select",
            }),
        }

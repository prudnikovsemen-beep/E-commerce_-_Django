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
        fields = ("email", "phone", "avatar", "country")

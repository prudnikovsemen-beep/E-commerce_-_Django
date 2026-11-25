from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.conf import settings
from users.forms import UserRegisterForm, UserLoginForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        send_mail(
            subject="Добро пожаловать!",
            message=f"{self.object.email}, спасибо за регистрацию в нашем сервисе!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )
        return response


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    pass


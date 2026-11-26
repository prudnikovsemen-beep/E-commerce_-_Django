# users/urls.py
from django.urls import path
from users.views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    ProfileView,
    profile_upload_avatar,
)

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/upload-avatar/", profile_upload_avatar, name="upload_avatar"),
]

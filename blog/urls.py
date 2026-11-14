from django.urls import path

from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),             # /blogs/ — список статей
    path("create/", BlogCreateView.as_view(), name="blog_create"),  # /blogs/create/ — создание
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"), # /blogs/<id>/ — просмотр
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"), # /blogs/<id>/update/
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"), # /blogs/<id>/delete/
]

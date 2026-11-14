from django.urls import path

from blog.views import (
    BlogListView,
    BlogArticleListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),              # /blogs/ — лента (статьи + видео)
    path("create/", BlogCreateView.as_view(), name="blog_create"),   # /blogs/create/
    path("articles/", BlogArticleListView.as_view(), name="blog_articles"),  # /blogs/articles/
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"), # /blogs/<id>/
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]

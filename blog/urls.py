from django.urls import path

from blog.views import (
    BlogListView,
    BlogArticleListView,
    BlogVideoListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),                       # /blogs/ — лента (статьи + видео)
    path("create/", BlogCreateView.as_view(), name="blog_create"),           # /blogs/create/
    path("articles/", BlogArticleListView.as_view(), name="blog_articles"),  # /blogs/articles/
    path("video/", BlogVideoListView.as_view(), name="blog_video_list"),     # /blogs/video/
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),         # /blogs/<id>/
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]

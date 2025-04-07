from django.urls import path
from .views import blog_list, blog_detail, blog_edit

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("post/<int:post_id>/", blog_detail, name="blog_detail"),
    path("post/<int:post_id>/edit/", blog_edit, name="blog_edit"),
]

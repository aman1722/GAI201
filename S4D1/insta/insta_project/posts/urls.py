from django.urls import path
from .views import PostListView, delete_post

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/delete/', delete_post, name='delete-post'),
]

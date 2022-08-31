from django.urls import path
from . import views
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    UserArticleListView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserArticleListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='post-detail'),
    path('post/new/', ArticleCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', ArticleUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', ArticleDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about"),
]

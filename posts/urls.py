from django.urls import path
from posts.views import PostListView,PostDetailView,PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    ]
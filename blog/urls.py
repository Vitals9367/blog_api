from django.urls import path, include
from blog.views import PostList

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
]

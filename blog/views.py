from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
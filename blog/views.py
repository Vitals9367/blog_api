from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
        
    
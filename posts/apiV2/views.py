from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView
from ..models import Posts
from .serializers import PostListSerializer,PostCreateSerializer

class PostListApiView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer

class PostDetailApiView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer

class PostCreateApiView(CreateAPIView):
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer




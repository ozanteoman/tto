from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveDestroyAPIView,CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView
from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin
from .pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

from ..models import Posts,Comments
from .serializers import PostListSerializer,PostCreateUpdateSerializer,PostDetailSerailizer,CommentListSerializer,CommentCreateSerializer,CommentDeleteUpdateSerializer


class PostListApiView(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields=("title","content")
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PostPageNumberPagination
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        query_set = self.queryset.all()
        return query_set.filter(user=self.request.user)

class PostDetailApiView(RetrieveAPIView):
    #lookup_field =
    #lookup_field_kwarg=
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerailizer

class PostUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #kullanıcı kendı blogunu güncellemesi için.

class PostDeleteApiView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostCreateUpdateSerializer

class PostCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comments.objects.all()
    serializer_class = CommentListSerializer

class CommentCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentEditApiView(RetrieveAPIView,DestroyModelMixin,UpdateModelMixin):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentDeleteUpdateSerializer

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)

    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)


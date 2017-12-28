from django.conf.urls import url
from .views import PostListApiView,PostDetailApiView,PostDeleteApiView,PostUpdateApiView,PostCreateApiView,CommentListApiView,CommentCreateApiView,CommentEditApiView

urlpatterns=[
    url(r'^posts/$',PostListApiView.as_view(),name="post-list"),
    url(r'^posts/(?P<pk>\d+)/$',PostDetailApiView.as_view(),name="post-detail"),
    url(r'^posts/(?P<pk>\d+)/update/$',PostUpdateApiView.as_view(),name="post-update"),
    url(r'^posts/(?P<pk>\d+)/delete/$',PostDeleteApiView.as_view(),name="post-delete"),
    url(r'^posts/create/$',PostCreateApiView.as_view(),name="post-create"),
    url(r"^comments/$",CommentListApiView.as_view(),name="comment-list"),
    url(r"^comments-create/$",CommentCreateApiView.as_view(),name="comment-create"),
    url(r"^comments/(?P<pk>\d+)/edit$",CommentEditApiView.as_view(),name="comment-edit")
]
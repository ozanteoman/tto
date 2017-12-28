from django.conf.urls import url
from .views import PostListApiView,PostDetailApiView,PostCreateApiView,PostUpdateApiView
urlpatterns=[
    url(r'^post-list/$',PostListApiView.as_view(),name="post-list"),
    url(r'^post-list/(?P<pk>\d+)/$',PostDetailApiView.as_view(),name="post-detail"),
    url(r'post-create/$',PostCreateApiView.as_view(),name="post-create"),
    url(r'post-list/(?P<pk>\d+)/edit/$',PostUpdateApiView.as_view(),name="post-update")
]

from django.conf.urls import url
from .views import posts_list,post_detay,post_update,post_delete,post_create,my_post_list


urlpatterns=[
    url(r'^post-list/$', posts_list,name="post-list"),
    url(r'^my-post-list/$', my_post_list,name="my-post-list"),
    url(r'^post-detay/(?P<pk>\d+)/$', post_detay,name="post-detay"),
    url(r'^post-create/$', post_create,name="post-create"),
    url(r'^post-update/(?P<pk>\d+)/$', post_update,name="post-update"),
    url(r'^post-delete/(?P<pk>\d+)$', post_delete,name="post-delete"),
]
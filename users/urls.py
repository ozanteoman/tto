from django.conf.urls import url
from .views import user_create,user_logout,user_login

urlpatterns=[
    url(r'^user-login/$', user_login,name="user-login"),
    url(r'^user-create/$', user_create,name="user-create"),
    url(r'^user-logout/$', user_logout,name="user-logout"),
]
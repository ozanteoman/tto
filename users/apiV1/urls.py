from django.conf.urls import url
from .views import UserCreateApiView,UserLoginApiView

urlpatterns=[
    url(r"^user-create/$",UserCreateApiView.as_view(),name="user-create"),
    url(r"^user-login/$",UserLoginApiView.as_view(),name="user-create"),

]
"""tto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
#include fonksiyonu ile diger app dosyalarının içindeki url
#dosyasına bağlantı köprüleme kurdum
#örneğin posts/post-list
#posts/post-detay
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/',include('posts.urls')),
    url(r'^posts-apiV1/',include("posts.apiV1.urls",namespace="posts-api")),
    url(r'^posts-apiV2/',include("posts.apiV2.urls",namespace="posts-api2")),
    url(r'^users-apiV1/',include("users.apiV1.urls",namespace="users-api")),
    url(r'api/auth/token/',obtain_jwt_token),
    url(r'^users/',include('users.urls'))

]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
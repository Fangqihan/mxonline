"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from users.views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from organization.views import TeacherListView
from django.views.static import serve
import xadmin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$', HomePageView.as_view(), name='homepage'),
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^user/', include('users.urls', namespace='users')),
    url(r'^course/', include('courses.urls', namespace='courses')),
    url(r'^org/', include('organization.urls', namespace='orgs')),
    url(r'^operation/', include('operation.urls', namespace='operation')),
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    # ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]

if settings.DEBUG:
    # 在开发模式下，用户上传到media文件夹的文件可以按照设定的路径查找，但仅限于开发模式；
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
else:
    # 保证项目固定的静态文件可以正常加载,按照设定的路径查找；
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]

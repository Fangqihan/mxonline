from django.conf.urls import url, include
from .views import OrgListView, TeacherListView
from .views import OrgHomePage, OrgCourseView, OrgDescriptionView, OrgTeachersView, AddFavorView, TeacherDetailView


urlpatterns = [
    #机构页面相关的url配置
    url(r'^list/$', OrgListView.as_view(), name='org_list'),    # 机构列表页
    url(r'^home/(?P<org_id>[0-9]+)/$', OrgHomePage.as_view(), name='org_homepage'), # 机构详情页主页面
    url(r'^courses/(?P<org_id>[0-9]+)/$', OrgCourseView.as_view(), name='courses'), # 机构课程
    url(r'^des/(?P<org_id>[0-9]+)/$', OrgDescriptionView.as_view(), name='description'), #机构简介
    url(r'^teachers/(?P<org_id>[0-9]+)/$', OrgTeachersView.as_view(), name='teachers'), #机构的教师列表

    #教师页面相关的url配置
    url(r'^teacher_detail/(?P<teacher_id>[0-9]+)/$', TeacherDetailView.as_view(), name='teacher_detail'),


    url(r'^add_fav/$', AddFavorView.as_view(), name='add_favor'),


]

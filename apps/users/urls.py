from django.conf.urls import url
from .views import LoginView, logout_user, RegisterView, ActivateUserView, active_fail, active_success, ForgetPwdView, \
    ResetPwdView, UserCenterInfoView, SendEmailCodeView, ChangeEmailView, ChangePwdView, ImageUploadView, MyCourseView, \
    UserFavorCourseView, UserFavorTeachersView, UserFavorOrgsView, UserMessagesView



urlpatterns = [
    url('^login/$', LoginView.as_view(), name='login'),  # 用户登录
    url('^register/$', RegisterView.as_view(), name='register'),  # 注册新用户
    url('^logout/$', logout_user, name='logout'), # 注销当前用户
    url('^activate/(?P<code>.{16})/$', ActivateUserView.as_view(), name='activate'),#激活用户

    url('^active_failed/$', active_fail, name='active_failed'),
    url('^active_success/$', active_success, name='active_success'),

    url('^forget_pwd/$', ForgetPwdView.as_view(), name='forget_pwd'), # 登录页面忘记密码
    url('^reset_pwd/$', ResetPwdView.as_view(), name='reset_pwd'),  # 重置密码

    #在用户中心进行的相关操作
    url('^send_email_code/$', SendEmailCodeView.as_view(), name='send_email_code'),  # 发送邮箱验证码
    url('^change_email/$', ChangeEmailView.as_view(), name='change_mail'),
    url('^change_password/$', ChangePwdView.as_view(), name='change_pwd'),  # 修改密码
    url('^image_upload/$', ImageUploadView.as_view(), name='change_image'),  # 修改图片
    url('^user_course/$', MyCourseView.as_view(), name='user_course'),    # 用户学习课程

    url('^info/$', UserCenterInfoView.as_view(), name='user_center'),
    url('^favor/course/$', UserFavorCourseView.as_view(), name='fav_course'),  # 用户收藏课程
    url('^favor/orgs/$', UserFavorOrgsView.as_view(), name='fav_orgs'),  # 用户收藏机构
    url('^favor/teachers/$', UserFavorTeachersView.as_view(), name='fav_teachers'),  # 用户收藏教师
    url('^messages/$', UserMessagesView.as_view(), name='user_messages'),  # 用户消息

]

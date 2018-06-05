from django.conf.urls import url, include
from .views import UserAskView, ModifyEmailView, ModifyPasswordView



urlpatterns = [
    url(r'^add_ask/$', UserAskView.as_view(), name='user_ask'),#用户咨询

    url(r'^modify_email/$', ModifyEmailView.as_view(), name='modify_email'),
    url(r'^modify_password/$', ModifyPasswordView.as_view(), name='modify_password'),
    # url(r'^send_email_code/$', SendEmailCodeView.as_view(), name='send_email_code'),

]

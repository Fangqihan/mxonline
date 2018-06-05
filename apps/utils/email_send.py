from django.core.mail import send_mail

from random import Random
from users.models import EmailVerifyRecord
import datetime
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM
import random, string


def generate_random_str(num):
    #生成指定位数的字符串
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num))


def send_email(email, send_type=""):
    '''发送邮件,注册或者重置密码'''
    email_record = EmailVerifyRecord()
    if send_type == "change_email":
        code = generate_random_str(4)
    else:
        code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.send_time = datetime.datetime.now()
    email_record.save()
    email_title = ""
    email_body = ""
    if send_type == 'register':
        email_title = 'MXonline在线网注册激活连接'
        email_body = '请点击下面的链接重置密码: http://127.0.0.1:8000/users/activate/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = 'MXonline在线网密码重置连接'
        email_body = '请点击下面的链接激活的你的账号: http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'change_email':
        email_title = 'MXonline在线网绑定邮箱更改链接'
        email_body = '请复制您的验证码 : {0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass





import json
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from pure_pagination import Paginator, PageNotAnInteger

from courses.models import Course
from operation.models import UserCourses, UserFavorite, UserMessages
from organization.models import CourseOrg, Teacher
from users.models import UserProfile, Banner
from apps.utils.email_send import send_email
from .forms import LoginForms, RegisterForms, ForgetPwdForms, ResetPwdForms, ModifyEmailForm, UploadImageForm
from .models import EmailVerifyRecord


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {
        })

    def post(self, request):
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            # 提取对应的用户
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index/')
            else:
                return render(request, 'login.html', {
                    'msg':'用户名不存在',
                })
        else:
            return render(request, 'login.html', {
                'login_form': login_form,
                'msg':'用户名或密码输入有误'
            })


def logout_user(request):
    logout(request)
    return render(request, 'login.html', {
    })


class HomePageView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_courses = Course.objects.all()
        all_recommended_courses = Course.objects.filter(recommend=True)
        banners = Banner.objects.all().order_by('index')
        if all_recommended_courses:
            pass
        else:
            all_recommended_courses = all_courses

        if len(all_courses)> 6:  # 取前6位的课程显示
            all_courses = all_courses[:6]
        return render(request, 'index.html', {
            'all_orgs':all_orgs,
            'all_courses':all_courses,
            'all_recommended_courses':all_recommended_courses,
            'banners':banners
        })


from django.db.models import Q


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForms()
        return render(request, 'register.html', {
            'register_form':register_form,
        })


    def post(self, request):
        regitser_form = RegisterForms(request.POST, request.FILES)

        if regitser_form.is_valid():
            username = regitser_form.cleaned_data['username']
            avatar = regitser_form.files.get('avatar')
            pass_word = regitser_form.cleaned_data['password1']
            user = UserProfile()
            user.is_active = True
            user.username = username
            user.image = avatar
            user.password = make_password(pass_word)
            user.is_active = False
            user.save()
            #  此处省略邮箱激活验证
            # send_email(username, 'register')
            return render(request, 'login.html', {
            })

        else:
            errors = regitser_form.errors
            print(errors)
            return render(request, "register.html", {'register_form': regitser_form,'errors':errors})



class ActivateUserView(View):
    def get(self, request, code):
        email_record = EmailVerifyRecord.objects.filter(code=code)
        if email_record:#传输过来的code是否是之前发送的
            record = email_record[0]
            email = record.email
            user = UserProfile.objects.get(email=email)
            user.is_active = 1
            user.save()
            return redirect('/users/active_success/')

        else:
            return redirect('/users/active_failed/')


class MyBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
            else:
                pass
        except:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None


def active_fail(request):
    return render(request, 'register_code_fail.html')


def active_success(request):
    return render(request, 'activate_success.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPwdForms()
        return render(request, 'forget_pwd.html',{
            'forget_form':forget_form,
        })

    def post(self, request):
        forget_form = ForgetPwdForms(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            user_profile = UserProfile.objects.filter(Q(email=email)|Q(username=email))
            if user_profile:
                # 存在相关用户,跳转至密码重置页面
                return render(request, 'password_reset.html', {
                    'email':email,
                })

            # 不存在相关用户
            return render(request, 'forget_pwd.html', {
                'forget_form':forget_form,
                'msg':'对不起，该邮箱未被注册'
            })

        else:
            errors = forget_form.errors
            print(errors)
            return render(request, 'forget_pwd.html', {
                'forget_form':forget_form,
                'msg': '您输入的邮箱或验证码格式有误'
            })


class ResetPwdView(View):
    def get(self, request):
        return render(request, 'password_reset.html')

    def post(self, request):
        pwd_form = ResetPwdForms(request.POST)

        if pwd_form.is_valid():
            if pwd_form.cleaned_data['password1'] != pwd_form.cleaned_data['password2']:
                return render(request, 'password_reset.html', {
                    "msg":"密码不一致",
                })

            else:
                #输入经过form的验证，且两次输入相同
                if request.POST.get('email'):
                    email = request.POST.get('email')
                    user_profile = UserProfile.objects.get(Q(email=email)|Q(username=email))
                    user_profile.password = make_password(pwd_form.cleaned_data['password1'])
                    user_profile.save()
                    return redirect('/user/login/')
                else:
                    return render(request, 'org_error.html')

        else:
            #密码输入有误
            return render(request, 'password_reset.html', {
                "msg": '密码至少要有六位数',
            })



class UserCenterInfoView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'usercenter-info.html', {
            })
        else:
            # 若未登录，则返回登录界面
            return render(request, 'login.html')

    def post(self, request):
        if request.user.is_authenticated:
            nick_name = request.POST.get('nick_name', '')

            birthday = request.POST.get('birthday', '')
            birthday = birthday.replace('年', '-').replace('月', '-').replace('日', '')
            date_str = birthday
            fmt = '%Y-%m-%d'
            birthday = datetime.strptime(date_str, fmt).date()
            gender = request.POST.get('gender', '')
            address = request.POST.get('address', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            user = request.user
            user.nick_name = nick_name
            user.birthday = birthday
            user.gender = gender
            user.address = address
            user.mobile = mobile
            user.email = email
            user.save()
            return HttpResponse(json.dumps({'status': 'success', 'msg': '保存成功'}), content_type='application/json')

        else:
            return render(request, 'login.html')


class SendEmailCodeView(View):
    #发送邮件验证码
    def get(self, request):
        if request.user.is_authenticated:
            email = request.GET.get('email', '')
            if email:
                user_profile_lst = UserProfile.objects.filter(email=email)
                #查看邮件是否已被注册
                if user_profile_lst:
                    return HttpResponse(json.dumps({'status': 'failure', 'msg': '邮箱已注册'}), content_type='application/json')
                else:
                    #邮箱未被注册，但是这里没有检查邮箱书写规范
                    send_email(email, 'change_email') #在调用发送函数过程中已经将发送的验证码和邮箱信息保存进数据库了
                    return HttpResponse(json.dumps({'status': 'success', 'msg': '邮箱已注册'}), content_type='application/json')

            else:
                return HttpResponse(json.dumps({'status': 'failure', 'msg': '请输入邮箱'}), content_type='application/json')

        else:
            return render(request, 'login.html')


class ChangeEmailView(View):
    def post(self, request):
        if request.user.is_authenticated:
            change_email_form = ModifyEmailForm(request.POST)
            if change_email_form.is_valid():    # 输入内容是否符合语法
                code = change_email_form.cleaned_data.get('code', '')
                email = change_email_form.cleaned_data.get('email', '')
                record_lst = EmailVerifyRecord.objects.filter(email=email)
                if record_lst:
                    record = EmailVerifyRecord.objects.get(email=email)
                    stored_code = record.code
                    if code == stored_code:
                        user = request.user
                        user.email = email
                        user.save()
                        return HttpResponse(json.dumps({'status': 'success', 'msg': '邮箱修改成功'}), content_type='application/json')
                    else:

                        return HttpResponse(json.dumps({'status': 'failure', 'msg': '验证码有误'}), content_type='application/json')

                return HttpResponse(json.dumps({'status': 'failure', 'msg': '邮件有误'}), content_type='application/json')

            else:
                return HttpResponse(json.dumps({'status': 'failure', 'msg': '输入内容有误'}), content_type='application/json')

        else:
            return render(request, 'login.html')


class ChangePwdView(View):
    def post(self, request):
        if request.user.is_authenticated:
            change_email_form = ResetPwdForms(request.POST)
            if change_email_form.is_valid():
                pwd1 = change_email_form.cleaned_data.get('password1', '')
                pwd2 = change_email_form.cleaned_data.get('password2', '')
                if pwd1 == pwd2:
                    user = request.user
                    user.password = make_password(pwd1)
                    user.save()
                    return HttpResponse(json.dumps({'status': 'success', 'msg': '修改成功'}), content_type='application/json')

                else:
                    return HttpResponse(json.dumps({'status': 'failure', 'msg': '密码输入不一致'}), content_type='application/json')

            else:
                return HttpResponse(json.dumps({'status': 'failure', 'msg': '密码有误'}), content_type='application/json')

        else:
            return render(request, 'login.html')


class ImageUploadView(View):
    '''在用户中心修改用户图像'''
    def post(self, request):
        if request.user.is_authenticated:
            image_form = UploadImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                user = request.user
                user.image = image_form.cleaned_data.get('image')
                user.save()
                return HttpResponse(json.dumps({'status': 'success', 'msg': '图像修改成功'}),
                                    content_type='application/json')
            else:
                return HttpResponse(json.dumps({'status': 'failure', 'msg': '图片有误'}),
                                    content_type='application/json')

        else:
            return render(request, 'login.html')


class MyCourseView(LoginRequiredMixin, View):
    #我的课程
    def get(self, request):
        user = request.user
        user_courses = UserCourses.objects.filter(user=user)
        return render(request, 'usercenter-mycourse.html', {
            'user_courses':user_courses
        })


class UserFavorCourseView(LoginRequiredMixin, View):
    #用户收藏的课程
    def get(self, request):
        user = request.user
        courses_lst = []
        user_favor_lst = UserFavorite.objects.filter(user_id=user.id, favor_type=1)
        for user_favor in user_favor_lst:
            id = user_favor.favor_id
            if Course.objects.filter(id=id):
                courses_lst.append(Course.objects.get(id=id))
            else:
                pass

        return render(request, "usercenter-userfavor-course.html", {
            'courses_lst':courses_lst

        })


class UserFavorOrgsView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        orgs_lst = []
        user_favor_lst = UserFavorite.objects.filter(user=user, favor_type=3)
        for user_favor in user_favor_lst:
            id = user_favor.favor_id
            if CourseOrg.objects.filter(id=id): #筛选出符合id的所有机构
                orgs_lst.append(CourseOrg.objects.get(id=id))
            else:
                pass
        return render(request, "usercenter-userfavor-orgs.html", {
            'orgs_lst':orgs_lst,

        })


class UserFavorTeachersView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        teachers_lst = []
        user_favor_lst = UserFavorite.objects.filter(user=user, favor_type=2)
        for user_favor in user_favor_lst:
            id = user_favor.favor_id
            if Teacher.objects.filter(id=id): #筛选出符合id的所有教师
                teachers_lst.append(Teacher.objects.get(id=id))
        return render(request, "usercenter-userfavor-teachers.html", {
            'teachers_lst':teachers_lst,
        })


class UserMessagesView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        user_msgs = UserMessages.objects.filter(user=user)
        if user_msgs:
            for user_msg in user_msgs:
                user_msg.has_read = True
                user_msg.save()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        paginator = Paginator(user_msgs, per_page=3, request=request)
        user_msgs = paginator.page(page)

        return render(request, "usercenter-message.html", {
            'user_msgs':user_msgs,

        })




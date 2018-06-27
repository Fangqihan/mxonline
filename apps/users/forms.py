from django import forms
from captcha.fields import CaptchaField


class LoginForms(forms.Form):
    password = forms.CharField(min_length=6, max_length=20, label='密码', required=True)
    username = forms.CharField(min_length=1, required=True, label='用户名', widget=forms.Textarea)


from django.forms import ValidationError
from users.models import UserProfile


class RegisterForms(forms.Form):
    username = forms.CharField(min_length=2, max_length=30,
                               error_messages={'required': '用户名不能为空', 'min_length': '用户名至少为两位'})
    password1 = forms.CharField(min_length=6, max_length=12,
                                error_messages={'required': '密码不能为空', 'min_length': '密码至少为两位'})
    password2 = forms.CharField(min_length=6, max_length=12,
                                error_messages={'required': '密码不能为空', 'min_length': '密码名至少为两位'})
    captcha = CaptchaField()

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if UserProfile.objects.filter(username=username):
            raise ValidationError("用户已注册")
        return username

    def clean(self):
        """密码一致性检测"""
        if self.cleaned_data.get('password1', '') == self.cleaned_data.get('password2', ''):
            return self.cleaned_data
        else:
            raise ValidationError("密码不一致")


class ForgetPwdForms(forms.Form):
    username = forms.CharField(max_length=30, error_messages={'required': '用户名不能为空'})
    captcha = CaptchaField()

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if not UserProfile.objects.filter(username=username):
            raise ValidationError("用户不存在")
        return username


class ResetPwdForms(forms.Form):
    password1 = forms.CharField(min_length=6, max_length=30)
    password2 = forms.CharField(min_length=6, max_length=30)
    username = forms.CharField(max_length=30)

    def clean(self):
        """密码一致性检测"""
        if self.cleaned_data.get('password1', '') == self.cleaned_data.get('password2', ''):
            return self.cleaned_data
        else:
            raise ValidationError("密码不一致")


class ModifyEmailForm(forms.Form):
    email = forms.EmailField(max_length=30, min_length=3)
    code = forms.CharField(min_length=4, max_length=4)


class UploadImageForm(forms.Form):
    image = forms.ImageField(max_length=100)

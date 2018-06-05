from django import forms


class UserAskForm(forms.Form):
    name = forms.CharField(max_length=20,min_length=2,error_messages={
        'min_length':'名字至少两位',
        'required':'用户名不能为空',
    })
    mobile = forms.CharField(min_length=11, max_length=11,error_messages={
        'min_length': '电话号码格式不对',
        'max_length': '电话号码格式不对',
        'required': '联系电话不能为空',
    })
    course_name = forms.CharField(min_length=1, max_length=30,error_messages={
        'required': '课程名称不能为空',
    })


from django.shortcuts import render, HttpResponse
from django.views import View
from operation.forms import UserAskForm
from .models import UserAsk
from django.db.models import Q

from datetime import datetime
import json


class UserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)

        if user_ask_form.is_valid():
            name = user_ask_form.cleaned_data.get('name')
            mobile = user_ask_form.cleaned_data.get('mobile')
            course_name = user_ask_form.cleaned_data['course_name']
            user_ask = UserAsk.objects.filter(name=name, mobile=mobile, course=course_name)

            if user_ask:
                msg={}
                msg['error'] = '对不起，你已经提交过相同的问题'
                return HttpResponse(json.dumps({'status':'fail', 'msg':msg}),
                                    content_type='application/json')

            user_ask = UserAsk(name=name, mobile=mobile, course=course_name, add_time=datetime.now())
            user_ask.save()
            return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')

        else:
            msg = user_ask_form.errors
            return HttpResponse(json.dumps({'status':'fail', 'msg':msg }),
                                content_type='application/json')


class ModifyEmailView(View):
    def post(self, request):

        return render(request, '', {

        })


class ModifyPasswordView(View):
    def post(self, request):

        return render(request, '', {

        })


def page_not_found(request):
    # 全局404处理函数，页面找不到
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    # 全局404处理函数,页面错误
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

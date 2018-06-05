from django.shortcuts import render, HttpResponse
from django.views import View
from .models import CourseOrg, City, Teacher
from courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import CourseOrg
from operation.models import UserFavorite

import json


class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = City.objects.all()
        # 通过url传输过来的参数，直接可以用GET方法取出；
        city_id = request.GET.get('city', '')
        # 要实现多层过滤，只需要保持all_orgs变量名称不变即可，供最后分页
        if city_id:
            # 如果city_id存在，则通过其进一步筛选
            all_orgs = all_orgs.filter(city_id=int(city_id))
        category = request.GET.get('ct', '')
        if category:
            # 如果category存在，则通过其进一步筛选
            all_orgs = all_orgs.filter(Q(category=category))

        top_three_orgs = all_orgs.order_by('-click_num')[:3]
        # 根据sort传入的值进行排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students_num')
        elif sort == 'courses':
            # 这个目前还无法解决，由于org是course的外键，可以通过对org实例化对象操作直接取出它所有的课程数目，但是这里的排序用不到，因为结果不是
            # org的model字段属性；
            all_orgs = all_orgs.order_by('-courses_num')
        orgs_num = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        paginator = Paginator(all_orgs, per_page=3, request=request)

        orgs = paginator.page(page)
        return render(request, 'org-list.html', {
            'orgs': orgs,
            'all_cities': all_cities,
            'city_id': city_id,
            'category': category,
            'sort': sort,
            'orgs_num': orgs_num,
            'top_three_orgs': top_three_orgs,
        })


class TeacherListView(View):

    def get(self, request):
        sort = request.GET.get('sort', '')
        all_teachers = Teacher.objects.all()
        hot_teachers = all_teachers.order_by('-favor_num')[:3]

        keywords = request.GET.get('keywords', '')
        if keywords:
            all_teachers = Teacher.objects.filter(Q(name__icontains=keywords)|Q(introduction__icontains=keywords)|Q(nick_name__icontains=keywords))

        teacher_num = all_teachers.count()

        if sort == "hot":
            all_teachers = all_teachers.order_by('-click_num')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        paginator = Paginator(all_teachers, per_page=5, request=request)
        teachers_page = paginator.page(page)

        return render(request, 'teachers-list.html', {
            'teachers_page': teachers_page,
            'teacher_num': teacher_num,
            'hot_teachers': hot_teachers,

        })


class OrgHomePage(View):
    def get(self, request, org_id):
        course_orgs = CourseOrg.objects.all().filter(id=int(org_id))
        # 查看在数据库中是否存在id相同的机构；
        if course_orgs:
            org = course_orgs[0]  # 取出机构
            all_courses = org.course_set.all()  # 取出本机构相关的所有课程

            # 判断当前用户机构是否被当前用户收藏
            org_favor = UserFavorite.objects.filter(favor_id=org.id, favor_type=3, user_id=request.user.id)

            if all_courses.count() > 4:
                # 当前页面显示不超过四个
                all_courses = all_courses[:4]

            all_teachers = org.teacher_set.all()  # 取出本机构相关的所有讲师
            if all_teachers.count() > 2:
                # 当前页面显示不超过两个
                all_teachers = all_teachers[:2]

            return render(request, 'org-detail-homepage.html', {
                'org': org,
                'all_courses': all_courses,
                'all_teachers': all_teachers,
                'org_favor': org_favor,
            })
        else:
            return render(request, 'org_error.html')


class OrgCourseView(View):
    def get(self, request, org_id):
        course_orgs = CourseOrg.objects.all().filter(id=org_id)
        # 查看在数据库中是否存在id相同的机构；
        if course_orgs:
            org = course_orgs[0]
            all_courses = org.course_set.all()

            return render(request, 'org-detail-course.html', {
                'org': org,
                'all_courses': all_courses
            })
        else:
            return render(request, 'org_error.html')


class OrgTeachersView(View):
    def get(self, request, org_id):
        course_orgs = CourseOrg.objects.all().filter(id=org_id)
        # 查看在数据库中是否存在id相同的机构；
        if course_orgs:
            org = course_orgs[0]
            all_teachers = org.teacher_set.all()
            return render(request, 'org-detail-teachers.html', {
                'org': org,
                'all_teachers': all_teachers,

            })
        else:
            return render(request, 'org_error.html')


class OrgDescriptionView(View):
    def get(self, request, org_id):
        course_orgs = CourseOrg.objects.all().filter(id=org_id)
        # 查看在数据库中是否存在id相同的机构；
        if course_orgs:
            org = CourseOrg.objects.get(id=org_id)
            return render(request, 'org-detail-desc.html', {
                'org': org,
            })
        else:
            return render(request, 'org_error.html')


class AddFavorView(View):
    """添加收藏,可以作为API供其他app使用"""

    def post(self, request):
        fav_type = request.POST.get('fav_type', '')
        fav_id = request.POST.get('fav_id', '')
        object = ''  # 初始化虚拟对象
        if int(fav_type) == 1:  # 判断传入类型是否是Course
            object = Course.objects.get(id=fav_id)
        elif int(fav_type) == 3:  # 判断传入类型是否是 CourseOrg
            object = CourseOrg.objects.get(id=fav_id)
        else:  # 判断传入类型是否是 Teacher
            object = Teacher.objects.get(id=fav_id)

        if request.user.is_authenticated():  # 判断当前发出请求的用户是否登录

            # 必须是当初发起收藏的用户才能够取消收藏，别的用户不能取消
            user_favors = UserFavorite.objects.filter(favor_id=int(fav_id), favor_type=int(fav_type),
                                                      user_id=request.user)
            # 判断数据库是否有相匹配的数据
            if user_favors:  # 取出UserFavorite实例化对象，进行取消收藏操作，并且修改相应的model的has_favor属性；
                user_favor = UserFavorite.objects.get(favor_id=int(fav_id), favor_type=int(fav_type),
                                                      user_id=request.user)
                user_favor.delete()
                object.favor_num -= 1
                if object.favor_num - 1 < 0:
                    object.favor_num = 0
                object.has_favor = False
                object.save()

                return HttpResponse(json.dumps({'status': 'success', 'msg': '收藏'}), content_type='application/json')
            else:  # 收藏
                user_favor = UserFavorite()
                user_favor.favor_type = fav_type
                user_favor.favor_id = fav_id
                user_favor.user = request.user
                user_favor.save()
                object.favor_num += 1
                object.favor_user_id = request.user.id
                object.save()
                return HttpResponse(json.dumps({'status': 'success', 'msg': '已收藏'}),
                                    content_type='application/json')

        else:
            return HttpResponse(json.dumps({'status': 'failed', 'msg': '用户未登录'}), content_type='application/json')


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teachers = Teacher.objects.filter(id=teacher_id)
        if teachers:
            teacher = Teacher.objects.get(id=teacher_id)
            teacher_courses = teacher.course_set.all()
            org = teacher.org

            teacher_favor = UserFavorite.objects.filter(favor_id=teacher.id, favor_type=2, user_id=request.user.id)
            org_favor = UserFavorite.objects.filter(favor_id=org.id, favor_type=3, user_id=request.user.id)

            # 按点击数取前三名的讲师
            hot_teachers = Teacher.objects.all().order_by('-click_num')
            if len(hot_teachers) > 3:
                hot_teachers = hot_teachers[:3]

            return render(request, "teacher-detail.html", {
                'teacher': teacher,
                'teacher_courses': teacher_courses,
                'org': org,
                'hot_teachers': hot_teachers,
                'teacher_favor': teacher_favor,
                'org_favor': org_favor,
            })

        else:
            return render(request, 'teacher_not_exist.html')

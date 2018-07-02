from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Course, Video
from operation.models import UserCourses, UserFavorite, CourseComments
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage

import json


class CourseListView(View):
    def get(self, request):
        sort = request.GET.get('sort', '')
        all_courses = Course.objects.all()
        recommend_courses = all_courses.filter(recommend=True)[:2]
        all_courses.order_by('students_num')

        # 取出关键词，若果有关键词，说明用使用了搜索功能，我们按照关键词对所有course对象进行筛选
        keywords = request.GET.get('keywords', '')
        if keywords:
            all_courses = Course.objects.filter(
                Q(name__icontains=keywords) | Q(description__icontains=keywords) | Q(detail__icontains=keywords) | Q(
                    degree__icontains=keywords) | Q(category__icontains=keywords))
        if sort == 'hot':
            all_courses = Course.objects.all().order_by('-click_num')
        elif sort == 'students':
            all_courses = Course.objects.all().order_by('-students_num')

        # 获取当前页码数
        try:
            page_num = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_num = 1

        p = Paginator(all_courses, per_page=6, request=request)
        # 此对象包含当前页的对象列表，在前端通过course_page.object_list取出
        course_page = p.page(page_num)
        return render(request, 'course-list.html', {
            'course_page': course_page,
            'recommend_courses': recommend_courses,
            'sort': sort,

        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course_list = Course.objects.filter(id=course_id)
        # 看数据库是否存与传入id匹配的课程
        if course_list:
            course = Course.objects.get(id=course_id)
            org = course.org
            course_favor = UserFavorite.objects.filter(favor_id=course.id, favor_type=1, user_id=request.user.id)
            org_favor = UserFavorite.objects.filter(favor_id=org.id, favor_type=3, user_id=request.user.id)
            user_courses = UserCourses.objects.filter(course_id=course.id)

            # 向数据库查询是否有相关的 UserCourse 类，因为可以通过这个model关联学这个课程的其他用户
            if user_courses:
                user_list = [user_course.user for user_course in user_courses]
                if len(user_list) > 3:
                    # 只显示前三位用学习课程用户对象
                    user_list = user_list[:3]
            else:
                # 说明没有用户学习过这个课程
                user_list = ''

            # 查找相同类别的其他课程，且从点击率由高到低排名，并取最靠前的，但是不能是自己
            related_courses = Course.objects.filter(category=course.category)
            related_course = ''
            if related_courses:
                # 查看相同类别的课程是否存在
                related_courses.order_by('-click_num')  # 按照点击率由高到低排序
                if len(related_courses) > 1:
                    # 必须有至少两个相同类别的课程，因为自身算一个
                    related_course = related_courses[0]
                    if related_course == course:  # 排除自己的可能性
                        related_course = related_courses[1]

            return render(request, 'course-detail.html', {
                'course': course,
                'user_list': user_list,
                'related_course': related_course,
                'course_favor': course_favor,
                'org_favor': org_favor,

            })

        else:
            # 查询的课程不存在
            return render(request, "course_not_exist.html")


class CourseVideoView(View):
    def get(self, request, course_id):
        if request.user.is_authenticated:
            course_lst = Course.objects.filter(id=int(course_id))
            if course_lst:  # 判断课程是否存在

                course = Course.objects.get(id=int(course_id))
                chapter_lst = course.chapter_set.all()  # 取出当前课程的所有章节对象
                recommended_courses = []  # 先初始化推荐课程列表,待后续使用

                user_courses_lst = UserCourses.objects.filter(course=course)  # 筛选出相同课程的 用户课程对象
                if len(user_courses_lst) >= 1:
                    users_lst = [user_course.user for user_course in user_courses_lst]  # 取出学过该课程的所有用户对象
                    for user in users_lst:
                        user_courses = UserCourses.objects.filter(user=user)
                        for user_course in user_courses:
                            if user_course.course in recommended_courses:
                                # 取出重复出现的课程，因为同一门课程可能有很多用户学习
                                pass
                            elif user_course.course == course:
                                # 排除传入id对应的课程
                                pass
                            else:
                                recommended_courses.append(user_course.course)

                # 实例化用户课程model对象，增加并保存当前用户与学习课程到数据库,如已经存在则无需操作；
                user_course = UserCourses.objects.filter(user=request.user, course=course)
                if user_course:
                    pass
                else:
                    user_course = UserCourses()
                    user_course.user = request.user
                    user_course.course = course
                    user_course.save()
                    # 修改课程学习人数
                    user_course.course.students_num += 1
                    user_course.course.save()

                return render(request, 'course_videos.html', {
                    'course': course,
                    'chapter_lst': chapter_lst,
                    'recommended_courses': recommended_courses,

                })

            else:
                # 所查询的课程不存在
                return render(request, 'course_not_exist.html')

        else:
            return render(request, 'login.html')


class VideoPlayView(View):

    def get(self, request, video_id, course_id):
        video_lst = Video.objects.filter(id=video_id)
        course_lst = Course.objects.filter(id=course_id)
        if video_lst:
            video = Video.objects.get(id=video_id)
            if course_lst:
                course = Course.objects.get(id=course_id)
                chapter_lst = course.chapter_set.all()  # 取出当前课程的所有章节对象
                recommended_courses = []  # 先初始化推荐课程列表,待后续使用
                user_courses_lst = UserCourses.objects.filter(course=course)  # 筛选出相同课程的 用户课程对象

                if len(user_courses_lst) >= 1:
                    users_lst = [user_course.user for user_course in user_courses_lst]  # 取出学过该课程的所有用户对象
                    for user in users_lst:
                        user_courses = UserCourses.objects.filter(user=user)
                        for user_course in user_courses:
                            if user_course.course in recommended_courses:
                                # 取出重复出现的课程，因为同一门课程可能有很多用户学习
                                pass
                            elif user_course.course == course:
                                # 排除传入id对应的课程
                                pass
                            else:
                                recommended_courses.append(user_course.course)

                return render(request, 'course-play.html', {
                    'course': course,
                    'chapter_lst': chapter_lst,
                    'recommended_courses': recommended_courses,
                    'video': video,

                })

            else:
                return render(request, 'course_not_exist.html', {

                })

        else:
            # 对应id的视频不存在
            return render(request, 'video_not_exist.html', {

            })


class CourseCommentView(View):
    def get(self, request, course_id):
        course_lst = Course.objects.filter(id=int(course_id))
        if course_lst:  # 判断课程是否存在
            course = Course.objects.get(id=int(course_id))
            all_comments = CourseComments.objects.filter(course=course)

            recommended_courses = []  # 先初始化推荐课程列表,待后续使用
            user_courses_lst = UserCourses.objects.filter(course=course)  # 筛选出相同课程的 用户课程对象
            if len(user_courses_lst) >= 1:
                users_lst = [user_course.user for user_course in user_courses_lst]  # 取出学过该课程的所有用户对象
                for user in users_lst:
                    user_courses = UserCourses.objects.filter(user=user)
                    for user_course in user_courses:
                        if user_course.course in recommended_courses:
                            # 取出重复出现的课程，因为同一门课程可能有很多用户学习
                            pass
                        elif user_course.course == course:
                            # 排除传入id对应的课程
                            pass
                        else:
                            recommended_courses.append(user_course.course)

            # 实例化用户课程model对象，增加并保存当前用户与学习课程到数据库,如已经存在则无需操作；
            user_course = UserCourses.objects.filter(user=request.user, course=course)
            if user_course:
                pass
            else:
                user_course = UserCourses()
                user_course.user = request.user
                user_course.course = course
                user_course.save()
                # 修改课程学习人数
                user_course.course.students_num += 1
                user_course.course.save()

            return render(request, 'course-comment.html', {
                'course': course,
                'all_comments': all_comments,
                'recommended_courses': recommended_courses,
            })

        else:
            # 所查询的课程不存在
            return render(request, 'course_not_exist.html')


class AddCommentView(LoginRequiredMixin, View):
    # 必须在登录的情况下发表评论
    def post(self, request):
        comments = request.POST.get('comments', '')
        course_id = request.POST.get('course_id', '')
        if Course.objects.filter(id=int(course_id)):
            course = Course.objects.get(id=int(course_id))
            course_comment = CourseComments()
            course_comment.user = request.user
            course_comment.course = course
            course_comment.comment = comments
            course_comment.save()
            return HttpResponse(json.dumps({'status': 'success', 'msg': '评论提交成功'}), content_type='application/json')

        else:
            return render(request, 'course_not_exist.html')

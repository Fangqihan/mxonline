from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course
from organization.models import CourseOrg, Teacher


class UserAsk(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    course = models.CharField(max_length=20, verbose_name='咨询课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name
        db_table='用户咨询'

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="评价用户")
    course = models.ForeignKey(Course, verbose_name='评价课程')
    comment = models.CharField(max_length=150, verbose_name='课程评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '用户课程评论'
        verbose_name_plural = verbose_name
        db_table='用户课程评论'


    def __str__(self):
        return self.comment


class UserMessages(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='接收用户')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    message = models.CharField(max_length=50, verbose_name='用户消息')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name
        db_table='用户消息'


    def __str__(self):
        return self.message



class UserCourses(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学习用户', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name='学习课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户学习课程'
        verbose_name_plural = verbose_name
        db_table='用户课程'


    #这里无需定义返回名称，直接在admin中定义list_display即可；


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    favor_type = models.IntegerField(choices=((3, '课程机构'), (2, '机构教师'), (1, '公开课程')), verbose_name='用户收藏类型')
    favor_id = models.IntegerField(default=0, verbose_name='收藏id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        db_table='用户收藏'













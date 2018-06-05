from datetime import datetime

from django.db import models
from users.models import UserProfile


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', max_length=50)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table='城市'

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(verbose_name='课程机构', max_length=20)
    category = models.CharField(choices=(('training_org', '培训机构'), ("school", '高校'), ('personal', '个人')), max_length=20)
    image = models.ImageField(upload_to="org/%Y/%m", max_length=100, verbose_name='机构图片')
    address = models.CharField(max_length=100, verbose_name='机构详细地址')
    description = models.TextField(verbose_name='机构介绍')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    favor_num = models.IntegerField(default=0, verbose_name='收藏数')
    city = models.ForeignKey(City, verbose_name='所在城市')
    students_num = models.IntegerField(default=0, verbose_name='学生人数')
    courses_num = models.CharField(default=0, verbose_name='课程数目', max_length=5)
    has_favor = models.BooleanField(default=False, verbose_name='是否收藏')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
        db_table='课程机构'

    def __str__(self):
        return self.name

    def get_courses_num(self):
        return self.course_set.all().count()



class Teacher(models.Model):
    name = models.CharField(verbose_name='教师姓名', max_length=20)
    image = models.ImageField(verbose_name='教师图片', max_length=100, upload_to='teacher/%Y/%m')
    work_year = models.IntegerField(verbose_name='工作年限', null=True, blank=True)
    work_position = models.CharField(max_length=20, verbose_name='工作职位', null=True, blank=True)
    age = models.IntegerField(verbose_name='年龄', default=0)
    introduction = models.CharField(max_length=100, verbose_name='教师描述')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    favor_num = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', max_length=20)
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    gender = models.CharField(choices=(('male','男'), ('female', '女')), verbose_name='性别', max_length=10, default='')
    company = models.CharField(max_length=20, default='',verbose_name='就职公司')
    nick_name = models.CharField(default='', verbose_name='昵称', max_length=10)

    #收藏用户id，若对应的id的用户收藏了此课程，那么favor_user_id = user.id,
    # has_favor = models.BooleanField(default=False, verbose_name='会否收藏',max_length=10)
    # has_favor_user = models.ForeignKey(UserProfile, verbose_name='收藏用户', default=1)
    # favor_user_id = models.IntegerField(default=0, verbose_name='收藏用户')#

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name
        db_table='教师'

    def __str__(self):
        return self.name













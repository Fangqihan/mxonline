from datetime import datetime
from django.db import models
from organization.models import CourseOrg, Teacher
from DjangoUeditor.models import UEditorField
from django.utils.safestring import mark_safe


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    description = models.CharField(max_length=100, verbose_name='课程描述')
    # detail = models.TextField(verbose_name='课程详情')
    # 配置ueditor
    detail = UEditorField(verbose_name='课程详情', width=600, height=300, imagePath="courses/ueditor/",
                            filePath="courses/ueditor/",default='')

    degree = models.CharField(choices=(('CJ', '初级'), ('ZJ', '中级'), ('GJ', '高级')), max_length=10)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    students_num = models.IntegerField(default=0, verbose_name='学习人数')
    category = models.CharField(max_length=20, verbose_name='课程类别')
    favor_num = models.IntegerField(default=0, verbose_name='收藏数')
    org = models.ForeignKey(CourseOrg, verbose_name="所属课程机构")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name='课程图片', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='课程添加时间')
    teacher = models.ForeignKey(Teacher, verbose_name="授课教师", blank=True, null=True)
    recommend = models.BooleanField(default=False, verbose_name='是否推荐', max_length=2)
    has_favor = models.BooleanField(default=False, verbose_name='是否收藏')
    notice = models.CharField(default='', verbose_name='课程须知', max_length=200)
    is_banner = models.BooleanField(default=False, verbose_name='广告课程')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        db_table = '课程'

    def __str__(self):
        return self.name

    def get_chap_num(self):
        return self.chapter_set.all().count()

    get_chap_num.short_description='章节数'

    def my_link(self):
        return mark_safe('<a href="https://www.baidu.com">链接</a>')
    my_link.short_description='章节数'


class Chapter(models.Model):
    name = models.CharField(max_length=50, verbose_name='章节名')
    course = models.ForeignKey(Course, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='课程添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        db_table = '章节'

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=50, verbose_name='视频名')
    chapter = models.ForeignKey(Chapter, verbose_name='所属章节')
    url = models.URLField(max_length=200, verbose_name='视频链接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='课程添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        db_table = '视频'

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    name = models.CharField(max_length=30, verbose_name='资料名称')
    course = models.ForeignKey(Course)
    download = models.FileField(upload_to='course/download/%Y/%m', verbose_name='下载', max_length=100)

    class Meta:
        verbose_name = '课程资源下载'
        verbose_name_plural = verbose_name
        db_table = '课程资源下载'

    def __str__(self):
        return self.name

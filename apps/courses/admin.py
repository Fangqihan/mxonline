from django.contrib import admin
from django.shortcuts import HttpResponse
from .models import Course, Chapter, Video, CourseResource
from django.utils.safestring import mark_safe

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','degree','learn_times','category','my_link']

    # def my_link(self,obj):
    #     return mark_safe('<a href="https://www.baidu.com">链接</a>')
    #
    # my_link.short_description = '自定制字段'
    #
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     return HttpResponse('自定制修改页面')
    #
    #
    # def changelist_view(self, request, extra_context=None):
    #     return HttpResponse('自定制列表页')


admin.site.register(Course, CourseAdmin)

class ChapterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chapter, ChapterAdmin)

class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)

class CourseResourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseResource, CourseResourceAdmin)

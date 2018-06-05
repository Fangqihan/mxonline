from django.contrib import admin
from .models import Course, Chapter, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    pass

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

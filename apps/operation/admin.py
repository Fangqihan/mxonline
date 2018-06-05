from django.contrib import admin
from .models import UserAsk, CourseComments, UserMessages, UserCourses, UserFavorite


class UserAskAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAsk, UserAskAdmin)

class CourseCommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseComments, CourseCommentsAdmin)

class UserMessagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserMessages, UserMessagesAdmin)

class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'add_time']

admin.site.register(UserCourses, UserCoursesAdmin)

class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'favor_type', 'favor_id', 'add_time']

admin.site.register(UserFavorite, UserFavoriteAdmin)
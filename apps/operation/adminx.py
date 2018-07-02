import xadmin
from operation.models import UserAsk, CourseComments, UserMessages


class UserAskAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'mobile', 'course', 'add_time']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'mobile', 'course']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'mobile', 'course', 'add_time']
    model_icon = 'fa fa-github'

xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommentsAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['user', 'course', 'comment', 'add_time']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['user', 'course', 'comment']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['user', 'course', 'comment']
    model_icon = 'fa fa-snowflake-o'


xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UserMessagesAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['user', 'has_read', 'message', 'add_time']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['user', 'has_read', 'message']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['user', 'has_read', 'message', 'add_time']


xadmin.site.register(UserMessages, UserMessagesAdmin)

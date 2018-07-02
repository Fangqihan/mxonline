import xadmin
from courses.models import Course, Chapter, Video


class CourseAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'degree', 'learn_times', 'category', 'favor_num', 'students_num', 'recommend', 'get_chap_num','my_link']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'degree', 'learn_times', 'category', 'favor_num', 'students_num',
                     'recommend']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式

    # 扩展功能4: 过滤器
    list_filter = ['name', 'degree', 'learn_times', 'category', 'favor_num', 'students_num', 'recommend']

    # 自定制图标
    model_icon = 'fa fa-columns'

    # 降序排列
    ordering=['-students_num']

    # 设置只读字段
    readonly_fields = ['name', 'degree', 'learn_times']

    # 设置不显示某些字段
    exclude = ['students_num']

    # 设置字段搜索样式

    # 设置在列表页页面可编辑的字段
    list_editable = ['degree','learn_times','recommend']

    # 函数显示

    # 页面定时刷新，可以在2和4s中选择，而且还可以取消刷新
    refresh_times = [2, 4]

    # ueditor插件步骤
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Course, CourseAdmin)


class ChapterAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'course']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'course']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'course']


xadmin.site.register(Chapter, ChapterAdmin)


class VideoAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'chapter', 'url']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'chapter', 'url']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'chapter', 'url']


xadmin.site.register(Video, VideoAdmin)


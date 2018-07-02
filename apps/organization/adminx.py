import xadmin
from organization.models import City, CourseOrg, Teacher


class CityAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'add_time']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'add_time']


xadmin.site.register(City, CityAdmin)


class CourseOrgAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'category', 'address', 'favor_num', 'click_num', 'city', 'students_num', 'courses_num',
                    'has_favor', 'add_time']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'category', 'address', 'favor_num', 'click_num', 'city', 'students_num', 'courses_num',
                     'has_favor']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'category', 'address', 'favor_num', 'click_num', 'city', 'students_num', 'courses_num',
                   'has_favor']

    # 只要是涉及到此model的外键都会显示查询，不会出现下拉框
    relfield_style = 'fk-ajax'


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    # 扩展功能1: 选择显示的字段
    list_display = ['name', 'age','gender','nick_name','work_year', 'work_position','company']
    # 扩展功能2: 添加字段搜索,筛选功能
    search_fields = ['name', 'age','gender','nick_name','work_year', 'work_position','company']  # 某些字段不能加,例如时间
    # 扩展功能3: 界面自带导出功能, 可以导出多种格式
    # 扩展功能4: 过滤器
    list_filter = ['name', 'age','gender','nick_name','work_year', 'work_position','company']


xadmin.site.register(Teacher, TeacherAdmin)

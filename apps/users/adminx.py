import xadmin


# 主题设置与菜单折叠
from xadmin import views


class BaseSetting(object):
    # 增加主题插件
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


# 全局页头和页脚配置
class GlobalSetting(object):
    site_title = '学习在线后台管理系统'
    site_footer = '学习在线'

    # 折叠左侧app菜单
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)


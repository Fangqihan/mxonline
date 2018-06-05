from django.contrib import admin
from .models import City, CourseOrg, Teacher


class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(City, CityAdmin)

class CourseOrgAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseOrg, CourseOrgAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)


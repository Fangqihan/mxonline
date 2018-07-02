from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord, Banner


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'gender', 'address']


admin.site.register(UserProfile, UserProfileAdmin)


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Banner, BannerAdmin)















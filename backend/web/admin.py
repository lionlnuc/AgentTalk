from django.contrib import admin
from web.models.user import UserProfile
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)#列表   逗号必须保留！！！为一个列表，查找时页面加载100条；若写成`raw_id_fields`,则添加用户时，名字为所有用户的下拉菜单

from django.contrib import admin

from .models import Article
from .models import Users
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_data')
    list_filter = ('pub_data',)


admin.site.register(Article, ArticleAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('usname', 'solotext')


admin.site.register(Users, UsersAdmin)

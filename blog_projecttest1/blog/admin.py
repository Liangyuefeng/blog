from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','link','index')
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')


admin.site.register(Category,CategoryAdmin)
admin.site.register(NewsArticle,NewsArticleAdmin)





class DataArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class FrontendArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class MobileArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class BackgroundArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class ManageArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class AIArticleArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','link','click_count')
class DoubanrecommendAdmin(admin.ModelAdmin):
    list_display = ('title','link')
class CsdnrecommendAdmin(admin.ModelAdmin):
    list_display = ('title','link')
class FunrecommendAdmin(admin.ModelAdmin):
    list_display = ('title','link')


admin.site.register(DataArticle,DataArticleAdmin)
admin.site.register(FrontendArticle,FrontendArticleAdmin)
admin.site.register(MobileArticle,MobileArticleAdmin)
admin.site.register(BackgroundArticle,BackgroundArticleAdmin)
admin.site.register(ManageArticle,ManageArticleAdmin)
admin.site.register(AIArticle,AIArticleArticleAdmin)
admin.site.register(Doubanrecommend,DoubanrecommendAdmin)
admin.site.register(Csdnrecommend,CsdnrecommendAdmin)
admin.site.register(Funrecommend,FunrecommendAdmin)

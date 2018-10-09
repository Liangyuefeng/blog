from django.db import models
from django.contrib.auth.models import User

#分类
class Category(models.Model):
    name=models.CharField(max_length=30,verbose_name='分类的名称')
    link=models.CharField(max_length=50,verbose_name='分类所在html',default=0)
    index=models.IntegerField(default=0,verbose_name='分类排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#最新资讯表
class NewsArticle(models.Model):
    title = models.CharField(max_length=200,verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0,verbose_name='点击次数')
    date_publish = models.CharField(max_length=300,verbose_name='发布时间')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')

    class Meta:
        verbose_name = '最新资讯'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 数据库表
class DataArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.CharField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '数据库表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 前端数据表
class FrontendArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '前端开发'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 移动开发
class MobileArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '移动开发'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 后台语言
class BackgroundArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '后台语言'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 运行维护
class ManageArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '运行维护'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# 人工智能
class AIArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    link = models.TextField(verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='点击次数')
    # date_publish = models.CharField(max_length=1000,verbose_name='发布时间')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '人工智能'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Doubanrecommend(models.Model):
    title = models.CharField(max_length=50,verbose_name='豆瓣推荐')
    link = models.TextField(verbose_name='书籍连接')

    class Meta:
        verbose_name = '豆瓣推荐'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Csdnrecommend(models.Model):
    title = models.CharField(max_length=50,verbose_name='csdn推荐')
    link = models.TextField(verbose_name='csdn链接')

    class Meta:
        verbose_name = 'csdn推荐'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Funrecommend(models.Model):
    title = models.CharField(max_length=50,verbose_name='段子')
    link = models.TextField(verbose_name='段子链接')

    class Meta:
        verbose_name = '段子推荐'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


#
# # #评论模型
# class ZComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(NewsArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '最新资讯评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class DComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(DataArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '数据库表评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class FComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(FrontendArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '前端表评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class MComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(MobileArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '移动开发评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class BComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(BackgroundArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '后台表评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class MAComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(ManageArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '运行维护评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content
#
# class AIComment(models.Model):
#     content = models.TextField(verbose_name='评论内容')
#     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='用户')
#     article = models.ForeignKey(AIArticle,on_delete=models.CASCADE,verbose_name='文章')
#
#     class Meta:
#         verbose_name = '人工智能评论'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.content





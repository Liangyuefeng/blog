# Generated by Django 2.0.2 on 2018-05-28 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '人工智能',
                'verbose_name_plural': '人工智能',
            },
        ),
        migrations.CreateModel(
            name='BackgroundArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '后台语言',
                'verbose_name_plural': '后台语言',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类的名称')),
                ('link', models.CharField(default=0, max_length=50, verbose_name='分类所在html')),
                ('index', models.IntegerField(default=0, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='csdnrecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='csdn推荐')),
                ('link', models.TextField(verbose_name='csdn链接')),
            ],
            options={
                'verbose_name': 'csdn推荐',
                'verbose_name_plural': 'csdn推荐',
            },
        ),
        migrations.CreateModel(
            name='DataArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '数据库表',
                'verbose_name_plural': '数据库表',
            },
        ),
        migrations.CreateModel(
            name='Doubanrecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='豆瓣推荐')),
                ('link', models.TextField(verbose_name='书籍连接')),
            ],
            options={
                'verbose_name': '豆瓣推荐',
                'verbose_name_plural': '豆瓣推荐',
            },
        ),
        migrations.CreateModel(
            name='FrontendArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '前端开发',
                'verbose_name_plural': '前端开发',
            },
        ),
        migrations.CreateModel(
            name='funrecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='段子')),
                ('link', models.TextField(verbose_name='段子链接')),
            ],
            options={
                'verbose_name': '段子推荐',
                'verbose_name_plural': '段子推荐',
            },
        ),
        migrations.CreateModel(
            name='ManageArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '运行维护',
                'verbose_name_plural': '运行维护',
            },
        ),
        migrations.CreateModel(
            name='MobileArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
            ],
            options={
                'verbose_name': '移动开发',
                'verbose_name_plural': '移动开发',
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('link', models.TextField(verbose_name='文章链接')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='点击次数')),
                ('date_publish', models.CharField(max_length=300, verbose_name='发布时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '最新资讯',
                'verbose_name_plural': '最新资讯',
            },
        ),
    ]

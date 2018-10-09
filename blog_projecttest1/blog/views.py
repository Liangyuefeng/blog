from django.shortcuts import render
import logging
from .models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.conf import settings




def global_setting(request):
    category_list = Category.objects.all()
    doubanrecom_list = Doubanrecommend.objects.all()
    csdnrecom_list = Csdnrecommend.objects.all()
    funrecom_list = Funrecommend.objects.all()
    return {
        "SITE_NAME":settings.SITE_NAME,
        "SITE_DESC":settings.SITE_DESC,
        "category_list":category_list,
        "doubanrecom_list":doubanrecom_list,
        "csdnrecom_list":csdnrecom_list,
        "funrecom_list":funrecom_list,

    }
logger = logging.getLogger('blog.views')
# # 首页函数
def index(request):
    try:
        # 最新文章获取
        article_list1 = NewsArticle.objects.all().order_by('-id')
        article_list2 = getPage(request, article_list1)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'index.html',locals())

def AI(request):
    try:
        article_list3=AIArticle.objects.all().order_by('-id')
        article_list4=getPage(request,article_list3)
        values = AIArticle.objects.get('id')

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'Ai.html',locals())


def Database(request):
    try:
        article_list5=DataArticle.objects.all().order_by('-id')
        article_list6=getPage(request,article_list5)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'database.html',locals())

def Frontend(request):
    try:
        article_list7=FrontendArticle.objects.all().order_by('-id')
        article_list8=getPage(request,article_list7)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'frontend.html',locals())

def Background(request):
    try:
        article_list9=BackgroundArticle.objects.all().order_by('-id')
        article_list10=getPage(request,article_list9)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'background.html',locals())

def Mobile(request):
    try:
        article_list11=MobileArticle.objects.all().order_by('-id')
        article_list12=getPage(request,article_list11)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'mobile.html',locals())

def Manage(request):
    try:
        article_list13=ManageArticle.objects.all().order_by('-id')
        article_list14=getPage(request,article_list13)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'manage.html',locals())



def getPage(request, article_list):
    paginator = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list




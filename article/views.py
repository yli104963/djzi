from django.shortcuts import render
# Create your views here.
from django.shortcuts import get_object_or_404
from .models import ArticlePost, ArticleSort, AboutMe, LinkFri, IndexSeo
from taggit.models import Tag
import markdown
from django.db.models.aggregates import Count
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


def article_list(request):
    articleslist = ArticlePost.objects.all()
    articleslist_tui = ArticlePost.objects.all()
    tags = Tag.objects.all()
    sorts = ArticleSort.objects.all()
    select_sort = ArticleSort.objects.annotate(num_posts=Count('articlepost'))
    articleslist_select = articleslist.order_by('-total_view')[:3]
    paginator = Paginator(articleslist, 5)
    page =  request.GET.get('page')
    articles = paginator.get_page(page)
    linkfri = LinkFri.objects.all()
    indexseo = IndexSeo.objects.all()
    context = {'indexseo':indexseo, 'linkfri':linkfri, 'articles':articles, 'tags':tags, 'sorts':sorts, 'select_sort':select_sort, 'articleslist_select': articleslist_select, 'articleslist_tui':articleslist_tui}
    return render(request, 'article/article-list.html', context)


def article_detail(request, id):
    articledetail = get_object_or_404(ArticlePost, id=id)
    articleslist = ArticlePost.objects.all()
    articleslist_tui = ArticlePost.objects.all()
    articledetail.total_view += 1
    articledetail.save(update_fields=['total_view'])
    tags = Tag.objects.all()
    sorts = ArticleSort.objects.all()
    articleslist_select = articleslist.order_by('-total_view')[:3]
    articledetail.asBody = markdown.markdown(articledetail.asBody,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])
    select_sort = ArticleSort.objects.annotate(num_posts=Count('articlepost'))
    context = {'articleslist_tui':articleslist_tui, 'select_sort':select_sort, 'articleslist_select':articleslist_select, 'articledetail':articledetail, 'tags':tags, 'sorts':sorts, 'select_sort':select_sort}
    context['previous_blog'] = ArticlePost.objects.filter(id__lt=articledetail.id).first()
    context['next_blog'] = ArticlePost.objects.filter(id__gt=articledetail.id).last()
    return render(request, 'article/article-detail.html', context)


def about_me(request):
    aboutme = AboutMe.objects.get(id=1)
    articleslist = ArticlePost.objects.all()
    articleslist_tui = ArticlePost.objects.all()
    tags = Tag.objects.all()
    sorts = ArticleSort.objects.all()
    aboutme.aboutmebody = markdown.markdown(aboutme.aboutmebody,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])
    select_sort = ArticleSort.objects.annotate(num_posts=Count('articlepost'))
    articleslist_select = articleslist.order_by('-total_view')[:3]
    context = {'aboutme':aboutme, 'tags': tags, 'sorts': sorts, 'select_sort': select_sort, 'articleslist_select': articleslist_select, 'articleslist_tui': articleslist_tui}
    return render(request, 'article/about.html', context)


def article_category(request, pk):
    articlesort = get_object_or_404(ArticleSort, pk=pk)
    sort_list = ArticlePost.objects.filter(arSort=articlesort).order_by('-poTime')
    articleslist = ArticlePost.objects.all()
    articleslist_tui = ArticlePost.objects.all()
    select_sort = ArticleSort.objects.annotate(num_posts=Count('articlepost'))
    tags = Tag.objects.all()
    sorts = ArticleSort.objects.all()
    articleslist_select = articleslist.order_by('-total_view')[:3]
    paginator = Paginator(sort_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articleslist_tui':articleslist_tui, 'select_sort':select_sort, 'articleslist_select':articleslist_select, 'articles':articles, 'tags': tags, 'sorts': sorts, 'articlesort':articlesort}
    return render(request, 'article/category.html',context)


def article_tag(request, pk):
    articleslist = ArticlePost.objects.all()
    select_sort = ArticleSort.objects.annotate(num_posts=Count('articlepost'))
    tags = Tag.objects.all()
    sorts = ArticleSort.objects.all()
    articleslist_select = articleslist.order_by('-total_view')[:3]
    t = get_object_or_404(Tag, pk=pk)
    tagslist = ArticlePost.objects.filter(arTags=t).order_by('poTime')
    articleslist_tui = ArticlePost.objects.all()
    paginator = Paginator(tagslist, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'sorts':sorts, 't':t, 'articleslist_tui':articleslist_tui, 'articles': articles, 'articleslist_select':articleslist_select, 'select_sort':select_sort, 'tags':tags, }
    return render(request, 'article/tags.html', context)


def robots(request):
    return render(request, 'robots.txt')

def go1(request):
    return HttpResponseRedirect('http://wpa.qq.com/msgrd?v=3&uin=xxxxxx&site=qq&menu=yes')

def go6(request):
    return HttpResponseRedirect('https://space.bilibili.com/xxxxx')

def go3(request):
    return HttpResponseRedirect('https://weibo.com/u/xxxxxx')

def go4(request):
    return HttpResponseRedirect('https://www.zhihu.com/people/xxxxx')
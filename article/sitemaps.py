from django.contrib.sitemaps import Sitemap
from .models import ArticlePost, ArticleSort, AboutMe
from django.urls import reverse

class ArticlePostSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.5

    def items(self):
        return ArticlePost.objects.all()

    def lastmod(self, obj):
        return obj.upTime

class ArticleSortSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.7

    def items(self):
        return ArticleSort.objects.all()

    def lastmod(self, obj):
        return obj.SortCreate


class AboutMeSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.4

    def items(self):
        return AboutMe.objects.all()

    def lastmod(self, obj):
        return obj.createtime


class staticSitmap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    def items(self):
        return ['article:article_list_index',]

    def location(self, item):
        return reverse(item)

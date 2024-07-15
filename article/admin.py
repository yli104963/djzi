from django.contrib import admin

# Register your models here.

from .models import ArticleSort, LinkFri, Banner, AdminProfile, IndexSeo, ArticlePost, SpecintroDes, AboutMe
from import_export.admin import ImportExportModelAdmin
from .resource import ArticleSortResource, LinkFriResource, BannerResource, AdminProfileResource, IndexSeoResource, ArticlePostResource


@admin.register(LinkFri)
class LinkFriColumnsAdmin(ImportExportModelAdmin):
    resource_class = LinkFriResource
    list_display = ['id', 'LinkName', 'LinkUrl', 'LinkCreate', 'LinkRel', 'is_active']
    list_filter = ['is_active', ]
    search_fields = ['LinkName', 'LinkUrl']
    list_per_page = 20
    list_editable = ('is_active', 'LinkName')
    date_hierarchy = 'LinkCreate'


@admin.register(ArticleSort)
class ArticleSortColumnsAdmin(ImportExportModelAdmin):
    resource_class = ArticleSortResource
    list_display = ['id', 'SortTitle', 'SortCreate',]
    list_filter = ['SortCreate',]
    search_fields = ['SortTitle', ]
    list_per_page = 20
    list_editable = ('SortTitle',)
    date_hierarchy = 'SortCreate'


@admin.register(Banner)
class BannerColumnsAdmin(ImportExportModelAdmin):
    resource_class = BannerResource
    list_display = ['id', 'BannerTitle', 'ImgAlt',]
    search_fields = ['BannerTitle', ]
    list_per_page = 10


@admin.register(AdminProfile)
class AdminProfileColumnsAdmin(ImportExportModelAdmin):
    resource_class = AdminProfileResource


@admin.register(IndexSeo)
class IndexSeoColumnsAdmin(ImportExportModelAdmin):
    resource_class = IndexSeoResource


@admin.register(ArticlePost)
class ArticlePostColumnsAdmin(ImportExportModelAdmin):
    resource_class = ArticlePostResource
    list_display = ['id', 'title', 'arSort', 'author', 'poTime', 'upTime', 'total_view',]
    search_fields = ['title']
    list_per_page = 10


@admin.register(SpecintroDes)
class SpecintroDesColumnsAdmin(ImportExportModelAdmin):
    resource_class = ArticleSortResource
    list_display = ['id', 'SpecintroTitle',]

admin.site.register(AboutMe)
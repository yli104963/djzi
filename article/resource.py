from import_export import resources

from .models import ArticleSort, LinkFri, Banner, AdminProfile, IndexSeo, ArticlePost, SpecintroDes


class ArticleSortResource(resources.ModelResource):
    class Meta:
        model = ArticleSort


class LinkFriResource(resources.ModelResource):
    class Meta:
        model = LinkFri


class BannerResource(resources.ModelResource):
    class Meta:
         model = Banner


class AdminProfileResource(resources.ModelResource):
    class Meta:
        model = AdminProfile


class IndexSeoResource(resources.ModelResource):
    class Meta:
        model = IndexSeo


class ArticlePostResource(resources.ModelResource):
    class Meta:
        model = ArticlePost


class SpecintroDesResource(resources.ModelResource):
    class Meta:
        model = SpecintroDes


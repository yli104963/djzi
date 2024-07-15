from django.db import models

# Create your models here.

# 导入时间模块
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField
from django.urls import reverse



# 创建分类模型
class ArticleSort(models.Model):
    SortTitle = models.CharField('文章分类', max_length=200)
    SortCreate = models.DateTimeField('分类创建时间', default=timezone.now)
    SortTitle_T = models.CharField('优化标题', max_length=200, default='')
    SortTitle_D = models.CharField('优化描述', max_length=200, default='')

    def __str__(self):
        return self.SortTitle

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article:article_category', args=[self.id])


# 创建友情链接模型
class LinkFri(models.Model):
    LinkName = models.CharField('链接名称', max_length=200)
    LinkUrl = models.URLField('友情链接', max_length=200)
    LinkCreate = models.DateTimeField('链接创建时间', default=timezone.now)
    is_active = models.BooleanField('是否显示', default=False)
    LinkRel = models.CharField('链接是否抓取', default='', max_length=200)

    def __str__(self):
        return self.LinkName

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

# 创建文章模型
class ArticlePost(models.Model):
    title = models.CharField('文章标题', max_length=200)
    meDes = models.TextField('文章描述', max_length=300)
    asBody = MDTextField('文本内容')
    arSort = models.ForeignKey(ArticleSort, on_delete=models.CASCADE, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    poTime = models.DateTimeField('发布时间', default=timezone.now)
    upTime = models.DateTimeField('更新时间', auto_now=True)
    arImg = models.ImageField('文章缩略图(740*400)', upload_to='article/%Y%m%d/', blank=True)
    arImgAlt = models.CharField('缩略图描述', max_length=200, blank=True)
    arTags = TaggableManager('文章标签', blank=True)
    total_view = models.PositiveIntegerField('文章浏览数', default=0)
    # comments = GenericRelation(Comment)


    class Meta:
        ordering = ('-id',)
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

# 创建轮播图模型
class Banner(models.Model):
    BannerTitle = models.CharField('轮播图标题', max_length=200, default='')
    BannerDes = models.CharField('轮播图描述', max_length=200, default='')
    BannerUrl = models.ImageField('轮播图链接(1400*800)', upload_to='banner/')
    ImgAlt = models.CharField('轮播图alt', max_length=200, default='')

    def __str__(self):
        return self.BannerTitle

    class Meta:
        verbose_name = '主轮播图'
        verbose_name_plural = verbose_name

# 创建个人信息模型
class AdminProfile(models.Model):
    AdminTitle = models.CharField('标题', max_length=200)
    AdminAvatarsImg = models.ImageField('首页作者图片(800*800)', upload_to='author/')
    AdminAvatarsImgAlt = models.CharField('首页作者图片描述', max_length=2000)
    AdminProfile = models.TextField('首页作者描述')

    def __str__(self):
        return self.AdminTitle

    class Meta:
        verbose_name = '个人信息'
        verbose_name_plural = verbose_name

# 创建特别技能模型
class SpecintroDes(models.Model):
    SpecintroTitle = models.CharField('技能标题', max_length=200)
    Specintro = models.TextField('技能介绍')

    def __str__(self):
        return self.SpecintroTitle
    class Meta:
        verbose_name = '特别技能'
        verbose_name_plural = verbose_name

# 创建首页模型
class IndexSeo(models.Model):
    IndexSeotTitle = models.CharField('首页标题', max_length=200)
    IndexSeoDes = models.TextField('首页描述')

    def __str__(self):
        return self.IndexSeotTitle

    class Meta:
        verbose_name = '首页TDK'
        verbose_name_plural = verbose_name


# 创建个人介绍模型
class AboutMe(models.Model):
    title = '个人介绍'
    aboutmebody = MDTextField('个人介绍')
    createtime = models.DateTimeField('发布时间', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '个人介绍'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article:about_me')
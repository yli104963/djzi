from django.urls import path
from . import views
app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='article_list_index'),
    path('about.html', views.about_me, name='about_me'),
    path('articlesort-<int:pk>.html', views.article_category, name='article_category'),
    path('articledetail/<int:id>.html', views.article_detail, name='article_detail'),
    path('articletag/<int:pk>.html', views.article_tag, name='article_tags'),
    path('robots.txt', views.robots, name='article-robots'),
    path('go1/', views.go1, name='go1'),
    path('go6/', views.go6, name='go6'),
    path('go3/', views.go3, name='go3'),
    path('go4/', views.go3, name='go4'),
]
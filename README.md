# 项目使用说明文档

## 项目简介

该项目是一个基于 Django 的博客系统，包含文章管理、分类、标签、友情链接、轮播图和个人信息等功能模块。

## 环境准备

1. 确保已安装 Python 3.x。
2. 安装 Django 及其他依赖库。在项目根目录下运行：

    ```bash
    pip install -r requirements.txt
    ```

## 数据库迁移

在项目根目录下运行以下命令以应用数据库迁移：
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    '''

### 创建超级用户

创建一个超级用户来访问 Django 管理后台：

    '''bash
    python manage.py createsuperuser
    '''

### 运行

项目根目录下运行：

    '''bash
    python manage.py runserver
    '''

### 文章管理

	•	文章列表：访问 http://127.0.0.1:8000/article/ 查看所有文章。
	•	文章详情：点击文章标题查看文章详情。
	•	按分类查看：访问 http://127.0.0.1:8000/article/articlesort-<分类ID>.html 查看分类下的文章。
	•	按标签查看：访问 http://127.0.0.1:8000/article/articletag-<标签ID>.html 查看标签下的文章。

### 个人介绍

	•	查看个人介绍：访问 http://127.0.0.1:8000/article/about.html 查看个人介绍。

### 友情链接

	•	查看友情链接。



### 模型概述

#### 文章分类模型（ArticleSort）

包含文章分类的基本信息。

#### 友情链接模型（LinkFri）

包含友情链接的基本信息。

#### 文章模型（ArticlePost）

包含文章的标题、描述、内容、分类、作者、发布时间等信息。

#### 轮播图模型（Banner）

包含轮播图的基本信息。

#### 个人信息模型（AdminProfile）

包含个人信息的基本描述。

#### 特别技能模型（SpecintroDes）

包含特别技能的介绍信息。

#### 首页模型（IndexSeo）

包含首页的 SEO 信息。

#### 个人介绍模型（AboutMe）

包含个人介绍的详细信息。

#### 管理后台

访问 http://127.0.0.1:8000/admin/ 进入 Django 管理后台，可以在此管理文章、分类、标签、友情链接、轮播图和个人信息等。

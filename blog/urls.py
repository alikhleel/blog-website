from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.get_users_page, name='users'),
    path('blogs/', views.get_blogs_page, name='blogs'),
    path('blogs/<int:blog_id>/', views.get_blog_detail_page, name='blog_detail'),
    path('blogs/<int:blog_id>/comments/', views.get_blog_comments_page, name='blog_comments'),
    path('categories/', views.get_categories_page, name='categories'),
]

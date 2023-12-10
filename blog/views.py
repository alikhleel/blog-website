from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template import loader

from .models import Post, Comment, Category


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def get_users_page(request):
    template = loader.get_template('users.html')
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def get_blogs_page(request):
    template = loader.get_template('blogs.html')
    blogs = Post.objects.all()
    context = {
        'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))


def get_blog_detail_page(request, blog_id):
    template = loader.get_template('blog_detail.html')
    post = Post.objects.get(id=blog_id)
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))


def get_blog_comments_page(request, blog_id):
    template = loader.get_template('blog_comments.html')
    comments = Comment.objects.filter(post=blog_id)
    context = {
        'post_title': Post.objects.get(id=blog_id).title,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))


def get_categories_page(request):
    template = loader.get_template('categories.html')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.utils import timezone
from .models import Post


def index(request):
    return render(request, 'index/index.html', {})

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'posts_list/posts_list.html', {'posts': posts})

def base_template(request):
	return render(request, 'base_template/base_template.html', {})
    
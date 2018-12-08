from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
    return render(request, 'projectone/index.html', {})

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'projectone/posts_list.html', {'posts': posts})

def base_template(request):
	return render(request, 'projectone/base_template.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'projectone/post_detail.html', {'post': post})
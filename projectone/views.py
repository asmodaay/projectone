from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})

def base_template(request):
    return render(request, 'base_template/base_template.html', {})
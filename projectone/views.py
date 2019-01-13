from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, ContactForm
from .models import Album
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

def index(request):
    albums = Album.objects.order_by('index').all()
    return render(request, 'projectone/index.html', {'albums': albums})

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'projectone/posts_list.html', {'posts': posts})

def base(request):
	return render(request, 'base.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'projectone/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'projectone/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'projectone/post_edit.html', {'form': form})

# Функция формы обратной связи
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['zhek9kulikov@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'zhek9kulikov@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'projectone/contact.html', {'form': form})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'projectone/thanks.html', {'thanks': thanks})
























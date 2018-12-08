from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts_list$', views.posts_list, name='posts_list'),
    url(r'^base$', views.base_template, name='base_template'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

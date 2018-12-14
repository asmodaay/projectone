from django.db import models

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Album(models.Model):
    
    img = models.CharField(max_length=120, verbose_name='Файл картинки')
    artist_name = models.CharField(max_length=120, verbose_name='Имя исполнителя')
    album_name = models.CharField(max_length=120, verbose_name='Название альбома')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    description = models.TextField(verbose_name='Описание')
    index = models.IntegerField(verbose_name='Индекс')
    alt = str(artist_name) + "  " + str(album_name)
    def __unicode__(self):
        return self.title
import datetime

from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    #article_author = models.CharField('Author name', default='Unknown', max_length=50)
    article_title = models.CharField('Название статьи', max_length=100)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def describe(self):
        return self.article_text[:100]

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Автор комментария', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    com_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.author_name


import datetime
from django.contrib.auth.models import User, UserManager, Group
from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from django.utils import timezone

def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        group = Group.objects.get(name='Commentators')
        user.groups.add(group)

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
    comment_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    #author_name = models.CharField('Автор комментария', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    com_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.comment_text



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        permission = Permission.objects.get(name='Can view poll')
        sender.user_permissions.add(permission)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''

'''class CustomUser(User):
    objects = UserManager()

    class Meta:
        proxy = True
        ordering = ('first_name',)'''



# Generated by Django 3.2.9 on 2021-11-09 16:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_alter_comment_com_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='com_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 16, 16, 16, 712351, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
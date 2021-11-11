# Generated by Django 3.2.9 on 2021-11-10 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211109_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_author',
        ),
        migrations.AlterField(
            model_name='comment',
            name='com_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 9, 9, 34, 598403, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]

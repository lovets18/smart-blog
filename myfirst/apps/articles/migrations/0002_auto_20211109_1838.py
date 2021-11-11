# Generated by Django 3.2.9 on 2021-11-09 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(default='Unknown', max_length=50, verbose_name='Author name'),
        ),
        migrations.AddField(
            model_name='comment',
            name='com_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 15, 38, 20, 942546, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]

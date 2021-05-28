# Generated by Django 3.1.7 on 2021-05-27 11:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0013_auto_20210526_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

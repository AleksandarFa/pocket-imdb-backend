# Generated by Django 3.1.7 on 2021-05-25 08:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_auto_20210525_0752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user_id', 'movie_id')},
        ),
    ]
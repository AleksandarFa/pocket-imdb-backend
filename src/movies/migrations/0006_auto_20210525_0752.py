# Generated by Django 3.1.7 on 2021-05-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210525_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='user_id',
            new_name='user',
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-19 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('DRAMA', 'Drama'), ('THRILLER', 'Thriller'), ('HORROR', 'Horror'), ('COMEDY', 'Comedy'), ('ACTION', 'Action')], default='ACTION', max_length=8)),
                ('coverImage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='files.file')),
            ],
        ),
    ]

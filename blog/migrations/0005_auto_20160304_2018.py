# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('alt', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image_blocks', models.ForeignKey(to='blog.ImageBlock')),
            ],
        ),
        migrations.CreateModel(
            name='PostPreview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('title', models.CharField(unique=True, max_length=100)),
                ('catching_text', models.TextField()),
                ('time_posted', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('post', models.OneToOneField(to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('preview_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='postpreview',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_blocks',
            field=models.ForeignKey(to='blog.TextBlock'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160304_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AlterField(
            model_name='imageblock',
            name='image',
            field=models.ImageField(upload_to=blog.models.post_path),
        ),
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(upload_to=b'tags/'),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

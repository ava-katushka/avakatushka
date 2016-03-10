# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160304_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_blocks',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_blocks',
        ),
        migrations.AddField(
            model_name='imageblock',
            name='post',
            field=models.ForeignKey(default=1, to='blog.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textblock',
            name='post',
            field=models.ForeignKey(default=1, to='blog.Post'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160309_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpreview',
            name='image',
            field=models.ImageField(upload_to=blog.models.postpreview_path),
        ),
    ]

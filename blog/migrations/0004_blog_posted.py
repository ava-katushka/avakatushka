# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 16, 11, 20, 52, 614068, tzinfo=utc), auto_now_add=True, db_index=True),
            preserve_default=False,
        ),
    ]

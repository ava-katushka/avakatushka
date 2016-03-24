# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160309_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('href', models.CharField(max_length=100)),
            ],
        ),
    ]

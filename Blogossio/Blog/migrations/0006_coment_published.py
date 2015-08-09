# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20150807_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
    ]

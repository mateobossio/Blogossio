# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_coment_fecha_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='fecha_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
        ),
    ]

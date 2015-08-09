# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20150803_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_pub'], 'verbose_name': 'Mi Post', 'verbose_name_plural': 'Todos mis posts'},
        ),
    ]

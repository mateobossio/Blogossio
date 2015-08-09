# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='fecha_pub',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 3, 14, 42, 4, 211180, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]

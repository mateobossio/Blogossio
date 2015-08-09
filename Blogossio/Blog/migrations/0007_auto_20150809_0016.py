# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_coment_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='published_in',
        ),
        migrations.DeleteModel(
            name='Mensajes',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20150806_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Mensaje')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_pub']},
        ),
        migrations.AddField(
            model_name='mensajes',
            name='published_in',
            field=models.ForeignKey(to='Blog.Post'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_txt', models.CharField(max_length=20, verbose_name=b'Titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_txt', models.CharField(max_length=20, verbose_name=b'Titulo del Comentario')),
                ('coment_txt', models.TextField(max_length=100, verbose_name=b'Comentatrio')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_txt', models.CharField(max_length=20, verbose_name=b'Titulo')),
                ('fecha_pub', models.DateTimeField(verbose_name=b'date published')),
                ('txt_resumen', models.CharField(max_length=50, verbose_name=b'Resumen')),
                ('txt_cont', models.TextField(verbose_name=b'Contenido')),
                ('categoria', models.ForeignKey(to='Blog.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(to='Blog.Post'),
        ),
    ]

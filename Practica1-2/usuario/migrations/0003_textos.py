# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180308_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170727_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=50, verbose_name='사이즈'),
        ),
    ]

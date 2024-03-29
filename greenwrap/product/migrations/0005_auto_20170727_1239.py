# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20170726_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productoptionprice',
            options={'ordering': ['-start_date'], 'verbose_name': '상품 옵션 가격', 'verbose_name_plural': '상품 옵션 가격 목록'},
        ),
        migrations.AlterField(
            model_name='productcategorysmall',
            name='title',
            field=models.CharField(max_length=50, verbose_name='소분류명'),
        ),
    ]

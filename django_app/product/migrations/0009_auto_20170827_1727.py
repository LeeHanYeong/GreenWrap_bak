# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20170827_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add_category_to_title',
        ),
        migrations.AddField(
            model_name='product',
            name='add_middle_category_to_title',
            field=models.BooleanField(default=False, verbose_name='상품명 앞에 중분류명을 추가'),
        ),
        migrations.AddField(
            model_name='product',
            name='add_small_category_to_title',
            field=models.BooleanField(default=False, verbose_name='상품명 앞에 소분류명을 추가'),
        ),
    ]

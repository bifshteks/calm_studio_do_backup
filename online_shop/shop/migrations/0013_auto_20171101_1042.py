# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20171025_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discount',
            field=models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах'),
        ),
    ]

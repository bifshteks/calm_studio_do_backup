# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Полная стоимость заказа'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-13 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20190418_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='post_script',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='订单留言'),
        ),
    ]

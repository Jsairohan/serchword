# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-10 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtext', '0003_auto_20190810_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='Column_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='words',
            name='Column_3',
            field=models.IntegerField(null=True),
        ),
    ]
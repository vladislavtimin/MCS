# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-08 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='addition_date',
            field=models.PositiveIntegerField(),
        ),
    ]

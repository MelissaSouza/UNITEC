# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20171124_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='DEFAULT VALUE', max_length=254),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default='DEFAULT VALUE', max_length=254),
        ),
    ]

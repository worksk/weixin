# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-09 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20190509_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='numb',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='todayorder',
            old_name='numb',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='todayorder',
            name='food_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todayorder',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]

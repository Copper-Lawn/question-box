# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stackunderflow', '0012_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stackunderflow.Answer'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackunderflow', '0007_question_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='', max_length=20)),
            ],
        ),
        
        migrations.AddField(
            model_name='question',
            name='keywords',
            field=models.ManyToManyField(null=True, to='stackunderflow.Keyword'),
        ),
    ]

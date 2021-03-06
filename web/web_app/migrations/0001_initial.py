# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spider', models.CharField(choices=[('new_york', 'NEY_YORK')], max_length=30)),
                ('status', models.CharField(choices=[(0, 'Starting'), (1, 'Processing'), (2, 'Success finished'), (3, 'Failed')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

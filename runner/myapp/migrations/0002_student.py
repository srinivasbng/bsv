# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-16 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

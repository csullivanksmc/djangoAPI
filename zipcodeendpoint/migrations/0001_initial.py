# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountyAdjacency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.TextField(blank=True, null=True)),
                ('county_geoid', models.TextField(blank=True, null=True)),
                ('adj_county', models.TextField(blank=True, null=True)),
                ('adj_county_geoid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'county_adjacency',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZipAdjacency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.TextField(blank=True, null=True)),
                ('adj_zip', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zip_adjacency',
                'managed': False,
            },
        ),
    ]

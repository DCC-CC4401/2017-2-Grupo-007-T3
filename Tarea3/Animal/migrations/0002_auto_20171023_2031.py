# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ONG', '0004_auto_20171023_2031'),
        ('Animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ong_responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ONG.ONG'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0003_merge_20171023_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
    ]

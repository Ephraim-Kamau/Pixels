# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='pix/'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_auto_20171026_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
    ]

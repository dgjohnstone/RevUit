# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_auto_20171121_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='book_app.Author'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-25 07:15
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20160425_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='thank_you_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]

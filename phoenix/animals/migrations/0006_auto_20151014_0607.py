# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_auto_20151008_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='dam',
            name='animal',
            field=models.ForeignKey(related_name='dam_animal', blank=True, to='animals.Animal', null=True),
        ),
        migrations.AddField(
            model_name='sire',
            name='animal',
            field=models.ForeignKey(related_name='sire_animal', blank=True, to='animals.Animal', null=True),
        ),
    ]

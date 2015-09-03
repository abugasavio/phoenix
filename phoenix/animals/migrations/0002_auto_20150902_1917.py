# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='birth_weight',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weaning_weight',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='yearling_weight',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

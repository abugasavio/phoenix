# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_animal_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dam',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='sire',
            name='animal',
        ),
        migrations.AlterField(
            model_name='milkproduction',
            name='butterfat',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=3),
        ),
    ]

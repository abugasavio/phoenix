# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_auto_20151103_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sire',
            name='animal',
        ),
    ]

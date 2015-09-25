# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20150923_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='dam',
            name='code',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]

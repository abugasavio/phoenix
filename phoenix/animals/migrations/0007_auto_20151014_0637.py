# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_auto_20151014_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breeder',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='modified_on',
        ),
        migrations.AddField(
            model_name='breeder',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AddField(
            model_name='breeder',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
    ]

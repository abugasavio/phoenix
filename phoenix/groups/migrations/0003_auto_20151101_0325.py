# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20151024_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(related_name='groups_group_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='group',
            name='modified_by',
            field=models.ForeignKey(related_name='groups_group_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
    ]

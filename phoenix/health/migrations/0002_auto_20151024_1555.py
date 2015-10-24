# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20151024_1555'),
        ('health', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='created_by',
            field=models.ForeignKey(related_name='health_treatment_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='group',
            field=models.ForeignKey(to='groups.Group', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='modified_by',
            field=models.ForeignKey(related_name='health_treatment_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
    ]

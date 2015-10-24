# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
        ('animals', '0002_auto_20151024_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(related_name='groups_group_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='group',
            name='dam',
            field=models.ForeignKey(related_name='dam_groups', blank=True, to='animals.Animal', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='modified_by',
            field=models.ForeignKey(related_name='groups_group_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='group',
            name='sire',
            field=models.ForeignKey(related_name='sire_groups', blank=True, to='animals.Animal', null=True),
        ),
    ]

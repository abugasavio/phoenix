# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20151024_1555'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0001_initial'),
        ('animals', '0002_auto_20151024_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_by',
            field=models.ForeignKey(related_name='records_note_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='note',
            name='group',
            field=models.ForeignKey(to='groups.Group', null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='modified_by',
            field=models.ForeignKey(related_name='records_note_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='animaldocument',
            name='animal',
            field=models.ForeignKey(related_name='documents', to='animals.Animal'),
        ),
    ]

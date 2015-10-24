# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=20, choices=[(None, b'------'), (b'female', 'Female'), (b'male', 'Male')])),
                ('start_birth_date', models.DateField(null=True, blank=True)),
                ('end_birth_date', models.DateField(null=True, blank=True)),
                ('breed', models.ForeignKey(blank=True, to='animals.Breed', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

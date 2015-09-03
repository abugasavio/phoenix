# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('created_by', models.ForeignKey(related_name='groups_group_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('dam', models.ForeignKey(related_name='dam_groups', blank=True, to='animals.Animal', null=True)),
                ('modified_by', models.ForeignKey(related_name='groups_group_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('sire', models.ForeignKey(related_name='sire_groups', blank=True, to='animals.Animal', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

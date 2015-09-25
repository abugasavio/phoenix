# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animals', '0002_auto_20150902_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('breed', models.ForeignKey(blank=True, to='animals.Breed', null=True)),
                ('breeder', models.ForeignKey(related_name='dam_breeder', blank=True, to='animals.Breeder', null=True)),
                ('created_by', models.ForeignKey(related_name='animals_dam_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_dam_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('breed', models.ForeignKey(blank=True, to='animals.Breed', null=True)),
                ('breeder', models.ForeignKey(related_name='sire_breeder', blank=True, to='animals.Breeder', null=True)),
                ('created_by', models.ForeignKey(related_name='animals_sire_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_sire_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='animal',
            name='breeder',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='code',
        ),
        migrations.AlterField(
            model_name='animal',
            name='dam',
            field=models.ForeignKey(related_name='dam', blank=True, to='animals.Dam', null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sire',
            field=models.ForeignKey(related_name='sire', blank=True, to='animals.Sire', null=True),
        ),
    ]

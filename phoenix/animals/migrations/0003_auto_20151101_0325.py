# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20151024_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='created_by',
            field=models.ForeignKey(related_name='animals_animal_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_animal_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='breed',
            name='created_by',
            field=models.ForeignKey(related_name='animals_breed_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='breed',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_breed_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='breeder',
            name='created_by',
            field=models.ForeignKey(related_name='animals_breeder_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='breeder',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_breeder_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='color',
            name='created_by',
            field=models.ForeignKey(related_name='animals_color_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='color',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_color_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='dam',
            name='created_by',
            field=models.ForeignKey(related_name='animals_dam_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='dam',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_dam_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='lactationperiod',
            name='created_by',
            field=models.ForeignKey(related_name='animals_lactationperiod_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='lactationperiod',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_lactationperiod_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='milkproduction',
            name='created_by',
            field=models.ForeignKey(related_name='animals_milkproduction_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='milkproduction',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_milkproduction_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='pregnancycheck',
            name='created_by',
            field=models.ForeignKey(related_name='animals_pregnancycheck_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='pregnancycheck',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_pregnancycheck_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_by',
            field=models.ForeignKey(related_name='animals_service_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='service',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_service_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AlterField(
            model_name='sire',
            name='created_by',
            field=models.ForeignKey(related_name='animals_sire_creations', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AlterField(
            model_name='sire',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_sire_modifications', to_field='id', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
    ]

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
        migrations.AddField(
            model_name='sire',
            name='created_by',
            field=models.ForeignKey(related_name='animals_sire_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='sire',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_sire_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='service',
            name='animal',
            field=models.ForeignKey(related_name='animal_services', to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='service',
            name='created_by',
            field=models.ForeignKey(related_name='animals_service_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='service',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_service_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='service',
            name='sire',
            field=models.ForeignKey(related_name='sire_services', to='animals.Sire'),
        ),
        migrations.AddField(
            model_name='pregnancycheck',
            name='animal',
            field=models.ForeignKey(related_name='pregnancy_checks', to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='pregnancycheck',
            name='created_by',
            field=models.ForeignKey(related_name='animals_pregnancycheck_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='pregnancycheck',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_pregnancycheck_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='pregnancycheck',
            name='service',
            field=models.ForeignKey(related_name='pregnancy_checks', blank=True, to='animals.Service', null=True),
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='animal',
            field=models.ForeignKey(related_name='milkproduction', to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='created_by',
            field=models.ForeignKey(related_name='animals_milkproduction_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_milkproduction_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='lactationperiod',
            name='animal',
            field=models.ForeignKey(related_name='animal_lactation_periods', to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='lactationperiod',
            name='calves',
            field=models.ManyToManyField(related_name='calf_lactation_periods', to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='lactationperiod',
            name='created_by',
            field=models.ForeignKey(related_name='animals_lactationperiod_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='lactationperiod',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_lactationperiod_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='dam',
            name='animal',
            field=models.ForeignKey(related_name='dam_animal', blank=True, to='animals.Animal', null=True),
        ),
        migrations.AddField(
            model_name='dam',
            name='breed',
            field=models.ForeignKey(blank=True, to='animals.Breed', null=True),
        ),
        migrations.AddField(
            model_name='dam',
            name='breeder',
            field=models.ForeignKey(related_name='dam_breeder', blank=True, to='animals.Breeder', null=True),
        ),
        migrations.AddField(
            model_name='dam',
            name='created_by',
            field=models.ForeignKey(related_name='animals_dam_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='dam',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_dam_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='color',
            name='created_by',
            field=models.ForeignKey(related_name='animals_color_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='color',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_color_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='breeder',
            name='created_by',
            field=models.ForeignKey(related_name='animals_breeder_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='breeder',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_breeder_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='breed',
            name='created_by',
            field=models.ForeignKey(related_name='animals_breed_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='breed',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_breed_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(blank=True, to='animals.Breed', null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='color',
            field=models.ForeignKey(blank=True, to='animals.Color', null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='created_by',
            field=models.ForeignKey(related_name='animals_animal_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='animal',
            name='dam',
            field=models.ForeignKey(related_name='dam', blank=True, to='animals.Dam', null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_animal_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='animal',
            name='sire',
            field=models.ForeignKey(related_name='sire', blank=True, to='animals.Sire', null=True),
        ),
    ]

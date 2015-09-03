# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('state', django_fsm.FSMField(default=b'open', max_length=50)),
                ('ear_tag', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=20, choices=[(None, b'------'), (b'female', 'Female'), (b'male', 'Male')])),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('birth_weight', models.IntegerField(max_length=4, null=True, blank=True)),
                ('weaning_date', models.DateField(null=True, blank=True)),
                ('weaning_weight', models.IntegerField(max_length=4, null=True, blank=True)),
                ('yearling_date', models.DateField(null=True, blank=True)),
                ('yearling_weight', models.IntegerField(max_length=4, null=True, blank=True)),
                ('code', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(related_name='animals_breed_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_breed_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(related_name='animals_breeder_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_breeder_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(related_name='animals_color_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_color_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LactationPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('animal', models.ForeignKey(related_name='animal_lactation_periods', to='animals.Animal')),
                ('calves', models.ManyToManyField(related_name='calf_lactation_periods', to='animals.Animal')),
                ('created_by', models.ForeignKey(related_name='animals_lactationperiod_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_lactationperiod_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MilkProduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('time', models.CharField(max_length=10, choices=[(b'am', 'Morning'), (b'pm', 'Evening')])),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('butterfat', models.DecimalField(max_digits=5, decimal_places=3)),
                ('date', models.DateField()),
                ('animal', models.ForeignKey(related_name='milkproduction', to='animals.Animal')),
                ('created_by', models.ForeignKey(related_name='animals_milkproduction_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_milkproduction_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PregnancyCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('result', models.CharField(max_length=20, choices=[(b'pregnant', 'Pregnant'), (b'open', 'Open')])),
                ('check_method', models.CharField(max_length=20, choices=[(b'palpation', 'Palpation'), (b'ultrasound', 'Ultrasound'), (b'observation', 'Observation'), (b'blood', 'Blood')])),
                ('date', models.DateField()),
                ('animal', models.ForeignKey(related_name='pregnancy_checks', to='animals.Animal')),
                ('created_by', models.ForeignKey(related_name='animals_pregnancycheck_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_pregnancycheck_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('method', models.CharField(default=b'artificial_insemination', max_length=30, choices=[(b'artificial_insemination', 'Artificial Insemination'), (b'natural_service', 'Natural Service')])),
                ('date', models.DateField()),
                ('notes', models.CharField(max_length=200, blank=True)),
                ('animal', models.ForeignKey(related_name='animal_services', to='animals.Animal')),
                ('created_by', models.ForeignKey(related_name='animals_service_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='animals_service_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('sire', models.ForeignKey(related_name='sire_services', to='animals.Animal')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pregnancycheck',
            name='service',
            field=models.ForeignKey(related_name='pregnancy_checks', blank=True, to='animals.Service', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(blank=True, to='animals.Breed', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='breeder',
            field=models.ForeignKey(related_name='sires', blank=True, to='animals.Breeder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='color',
            field=models.ForeignKey(blank=True, to='animals.Color', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='created_by',
            field=models.ForeignKey(related_name='animals_animal_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='dam',
            field=models.ForeignKey(related_name='dam_offsprings', blank=True, to='animals.Animal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='modified_by',
            field=models.ForeignKey(related_name='animals_animal_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='sire',
            field=models.ForeignKey(related_name='sire_offsprings', blank=True, to='animals.Animal', null=True),
            preserve_default=True,
        ),
    ]

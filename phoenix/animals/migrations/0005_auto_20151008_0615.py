# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_dam_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='sire',
            field=models.ForeignKey(related_name='sire_services', to='animals.Sire'),
        ),
    ]

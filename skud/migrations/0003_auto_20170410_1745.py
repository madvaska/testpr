# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skud', '0002_auto_20170410_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dep',
            name='parent',
            field=models.ForeignKey(null=True, to='skud.Dep'),
        ),
    ]

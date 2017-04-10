# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skud', '0003_auto_20170410_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dep',
            name='parent',
            field=models.ForeignKey(null=True, blank=True, to='skud.Dep'),
        ),
    ]

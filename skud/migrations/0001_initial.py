# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('fname', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

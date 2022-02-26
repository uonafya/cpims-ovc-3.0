# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0027_auto_20210212_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 12, 11, 53, 54, 253356)),
        ),
    ]

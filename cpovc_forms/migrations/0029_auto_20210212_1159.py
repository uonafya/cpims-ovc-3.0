# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0028_auto_20210212_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ovcmonitoring',
            name='monitoring_id',
        ),
        migrations.AddField(
            model_name='ovccaserecord',
            name='case_stage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ovcmonitoring',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 12, 11, 59, 49, 257309)),
        ),
    ]

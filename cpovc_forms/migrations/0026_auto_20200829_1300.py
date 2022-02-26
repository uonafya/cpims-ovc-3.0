# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0025_auto_20190806_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 13, 0, 55, 781055)),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='art_referral_completed_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='art_referral_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='date_of_event',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='referral_made_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]

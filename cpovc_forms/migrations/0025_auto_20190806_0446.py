# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0024_auto_20190722_0827'),
    ]

    operations = [
#        migrations.RemoveField(
#            model_name='ovcmonitoring',
#            name='monitoring_id',
#        ),
#        migrations.AddField(
#            model_name='ovcmonitoring',
#            name='id',
#            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
#        ),
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 4, 46, 35, 705231)),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='art_referral_completed_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 4, 46, 35, 703961), null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='art_referral_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 4, 46, 35, 703929), null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='date_of_event',
            field=models.DateField(default=datetime.datetime(2019, 8, 6, 4, 46, 35, 704035), null=True),
        ),
        migrations.AlterField(
            model_name='ovchivriskscreening',
            name='referral_made_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 4, 46, 35, 703818), null=True),
        ),
    ]

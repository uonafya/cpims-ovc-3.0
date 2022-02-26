# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0007_auto_20200829_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupLocation',
            fields=[
                ('area_id', models.IntegerField(serialize=False, primary_key=True)),
                ('area_name', models.CharField(max_length=100)),
                ('area_type_id', models.CharField(max_length=50)),
                ('area_code', models.CharField(max_length=10, null=True)),
                ('parent_area_id', models.IntegerField(null=True)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'list_location',
            },
        ),
        migrations.AddField(
            model_name='listanswers',
            name='answer_code',
            field=models.CharField(db_index=True, max_length=6, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0009_auto_20210212_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setuplist',
            name='item_id',
            field=models.CharField(max_length=7),
        ),
    ]

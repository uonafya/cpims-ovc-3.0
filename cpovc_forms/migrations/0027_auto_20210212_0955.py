# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0008_auto_20210212_0955'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_registry', '0002_auto_20180712_1945'),
        ('cpovc_forms', '0026_auto_20200829_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCBasicCategory',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('case_category', models.CharField(max_length=5)),
                ('case_sub_category', models.CharField(max_length=5, null=True)),
                ('case_date_event', models.DateField(default=django.utils.timezone.now)),
                ('case_nature', models.CharField(max_length=5)),
                ('case_place_of_event', models.CharField(max_length=5)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ovc_basic_category',
                'verbose_name': 'Basic Category',
                'verbose_name_plural': 'Basic Category',
            },
        ),
        migrations.CreateModel(
            name='OVCBasicCRS',
            fields=[
                ('case_id', models.UUIDField(default=uuid.uuid1, serialize=False, primary_key=True)),
                ('case_serial', models.CharField(default=b'XXXX', max_length=50)),
                ('case_reporter', models.CharField(max_length=5)),
                ('reporter_telephone', models.CharField(max_length=15, null=True)),
                ('reporter_county', models.CharField(max_length=3, null=True)),
                ('reporter_sub_county', models.CharField(max_length=3, null=True)),
                ('reporter_ward', models.CharField(max_length=100, null=True)),
                ('reporter_village', models.CharField(max_length=100, null=True)),
                ('case_date', models.DateField(default=django.utils.timezone.now)),
                ('perpetrator', models.CharField(max_length=5, null=True)),
                ('county', models.CharField(max_length=3)),
                ('constituency', models.CharField(max_length=3)),
                ('organization_unit', models.CharField(max_length=100)),
                ('case_landmark', models.CharField(max_length=50, null=True)),
                ('hh_economic_status', models.CharField(max_length=5)),
                ('family_status', models.CharField(max_length=5)),
                ('mental_condition', models.CharField(max_length=5)),
                ('physical_condition', models.CharField(max_length=5)),
                ('other_condition', models.CharField(max_length=5)),
                ('risk_level', models.CharField(max_length=5)),
                ('referral', models.CharField(default=b'ANNO', max_length=5)),
                ('referral_detail', models.CharField(max_length=200, null=True)),
                ('summon', models.CharField(default=b'ANNO', max_length=5)),
                ('case_narration', models.TextField(null=True)),
                ('longitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
                ('case_params', models.TextField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('case_comments', models.TextField(null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('account', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('case_org_unit', models.ForeignKey(blank=True, to='cpovc_registry.RegOrgUnit', null=True)),
            ],
            options={
                'db_table': 'ovc_basic_case_record',
                'verbose_name': 'Basic Case Record',
                'verbose_name_plural': 'Basic Case Records',
            },
        ),
        migrations.CreateModel(
            name='OVCBasicPerson',
            fields=[
                ('person_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('relationship', models.CharField(max_length=5, null=True)),
                ('person_type', models.CharField(max_length=5, choices=[(b'PTRD', b'Reporter'), (b'PTPD', b'Perpetrator'), (b'PTCH', b'Child'), (b'PTCG', b'Guardian')])),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50, null=True)),
                ('dob', models.DateField(null=True)),
                ('sex', models.CharField(max_length=5, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCBasicCRS')),
            ],
            options={
                'db_table': 'ovc_basic_person',
                'verbose_name': 'Basic Person',
                'verbose_name_plural': 'Basic Persons',
            },
        ),
        migrations.CreateModel(
            name='OvcCaseInformation',
            fields=[
                ('info_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('info_type', models.CharField(default=b'INFO', max_length=5)),
                ('info_item', models.CharField(max_length=6, null=True)),
                ('info_detail', models.TextField(null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ovc_case_info',
                'verbose_name': 'Case Information',
                'verbose_name_plural': 'Case Information',
            },
        ),
        migrations.CreateModel(
            name='OVCCaseLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ovc_case_location',
                'verbose_name': 'Case Area Location',
                'verbose_name_plural': 'Case Area Locations',
            },
        ),
        migrations.CreateModel(
            name='OvcCasePersons',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('person_relation', models.CharField(max_length=5, null=True)),
                ('person_first_name', models.CharField(max_length=100, null=True)),
                ('person_other_names', models.CharField(max_length=100, null=True)),
                ('person_surname', models.CharField(max_length=100, null=True)),
                ('person_type', models.CharField(default=b'PERP', max_length=5)),
                ('person_identifier', models.CharField(max_length=15, null=True)),
                ('person_dob', models.DateField(null=True)),
                ('person_sex', models.CharField(max_length=4, null=True, choices=[(b'SMAL', b'Male'), (b'SFEM', b'Female')])),
            ],
            options={
                'db_table': 'ovc_case_other_person',
                'verbose_name': 'Case Other Person',
                'verbose_name_plural': 'Case Other Persons',
            },
        ),
        migrations.CreateModel(
            name='OVCDreams',
            fields=[
                ('dreams_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('service_provided', models.CharField(max_length=250)),
                ('service_provider', models.CharField(max_length=250, null=True)),
                ('domain', models.CharField(max_length=10, null=True)),
                ('place_of_service', models.CharField(max_length=250, null=True)),
                ('date_of_encounter_event', models.DateField(default=django.utils.timezone.now)),
                ('service_grouping_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('event', models.ForeignKey(to='cpovc_forms.OVCCareEvents')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'ovc_dreams',
            },
        ),
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 12, 9, 55, 25, 415516)),
        ),
        migrations.AddField(
            model_name='ovccasepersons',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCCaseRecord', null=True),
        ),
        migrations.AddField(
            model_name='ovccasepersons',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson', null=True),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCCaseRecord'),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson'),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_location',
            field=models.ForeignKey(related_name='sub_location', to='cpovc_main.SetupLocation'),
        ),
        migrations.AddField(
            model_name='ovccaseinformation',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCCaseRecord', null=True),
        ),
        migrations.AddField(
            model_name='ovccaseinformation',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson', null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='case_record',
            field=models.ForeignKey(blank=True, to='cpovc_forms.OVCCaseRecord', null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccategory',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCBasicCRS'),
        ),
    ]

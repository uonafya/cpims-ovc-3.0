# Generated by Django 4.0.4 on 2022-05-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0008_alter_ovcbireferral_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovcbireferral',
            name='client_category',
            field=models.CharField(max_length=150),
        ),
    ]
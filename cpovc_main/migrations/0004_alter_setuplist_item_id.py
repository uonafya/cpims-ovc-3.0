# Generated by Django 4.0.4 on 2022-05-04 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0003_alter_admincapturesites_id_alter_admindownload_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setuplist',
            name='item_id',
            field=models.CharField(max_length=10),
        ),
    ]
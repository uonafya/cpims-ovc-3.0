# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth_provider.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('key', models.CharField(max_length=256)),
                ('secret', models.CharField(max_length=16, blank=True)),
                ('status', models.SmallIntegerField(default=1, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Canceled'), (4, 'Rejected')])),
                ('xauth_allowed', models.BooleanField(default=False, verbose_name=b'Allow xAuth')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token_key', models.CharField(max_length=32)),
                ('consumer_key', models.CharField(max_length=256)),
                ('key', models.CharField(max_length=255)),
                ('timestamp', models.PositiveIntegerField(db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.TextField(max_length=2083)),
                ('is_readonly', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=32, null=True, blank=True)),
                ('secret', models.CharField(max_length=16, null=True, blank=True)),
                ('token_type', models.SmallIntegerField(choices=[(1, 'Request'), (2, 'Access')])),
                ('timestamp', models.IntegerField(default=oauth_provider.models.default_token_timestamp)),
                ('is_approved', models.BooleanField(default=False)),
                ('verifier', models.CharField(max_length=10)),
                ('callback', models.CharField(max_length=2083, null=True, blank=True)),
                ('callback_confirmed', models.BooleanField(default=False)),
                ('consumer', models.ForeignKey(to='oauth_provider.Consumer')),
                ('scope', models.ForeignKey(blank=True, to='oauth_provider.Scope', null=True)),
                ('user', models.ForeignKey(related_name=b'tokens', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('oauth_provider.scope',),
        ),
    ]

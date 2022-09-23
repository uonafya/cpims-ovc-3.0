# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from oauth_provider.compat import AUTH_USER_MODEL

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table(u'oauth_provider_resource', u'oauth_provider_scope')
        db.rename_column(u'oauth_provider_token', u'resource_id', u'scope_id')
        db.send_create_signal(u'oauth_provider', [u'Scope'])

    def backwards(self, orm):
        db.rename_table(u'oauth_provider_scope', u'oauth_provider_resource')
        db.rename_column(u'oauth_provider_token', u'scope_id', u'resource_id')
        db.send_create_signal(u'oauth_provider', [u'Resource'])

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'%s' % AUTH_USER_MODEL: {
            'Meta': {'object_name': AUTH_USER_MODEL.split('.')[-1]},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'oauth_provider.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s']" % AUTH_USER_MODEL, 'null': 'True', 'blank': 'True'}),
            'xauth_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'oauth_provider.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'token_key': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'oauth_provider.scope': {
            'Meta': {'object_name': 'Scope'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_readonly': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.TextField', [], {'max_length': '2083'})
        },
        u'oauth_provider.token': {
            'Meta': {'object_name': 'Token'},
            'callback': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'null': 'True', 'blank': 'True'}),
            'callback_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth_provider.Consumer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth_provider.Scope']"}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'default': '1382371788L'}),
            'token_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tokens'", 'null': 'True', 'to': u"orm['%s']" % AUTH_USER_MODEL}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
    }

    complete_apps = ['oauth_provider']
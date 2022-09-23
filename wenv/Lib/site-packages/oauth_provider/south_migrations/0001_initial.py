# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from oauth_provider.compat import AUTH_USER_MODEL
from django.db import models
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Nonce'
        db.create_table('oauth_provider_nonce', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token_key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('oauth_provider', ['Nonce'])

        # Adding model 'Resource'
        db.create_table('oauth_provider_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.TextField')(max_length=2083)),
            ('is_readonly', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('oauth_provider', ['Resource'])

        # Adding model 'Consumer'
        db.create_table('oauth_provider_consumer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[AUTH_USER_MODEL], null=True, blank=True)),
        ))
        db.send_create_signal('oauth_provider', ['Consumer'])

        # Adding model 'Token'
        db.create_table('oauth_provider_token', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('token_type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')(default=1327884735L)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tokens', null=True, to=orm[AUTH_USER_MODEL])),
            ('consumer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth_provider.Consumer'])),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth_provider.Resource'])),
            ('verifier', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('callback', self.gf('django.db.models.fields.CharField')(max_length=2083, null=True, blank=True)),
            ('callback_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('oauth_provider', ['Token'])


    def backwards(self, orm):
        
        # Deleting model 'Nonce'
        db.delete_table('oauth_provider_nonce')

        # Deleting model 'Resource'
        db.delete_table('oauth_provider_resource')

        # Deleting model 'Consumer'
        db.delete_table('oauth_provider_consumer')

        # Deleting model 'Token'
        db.delete_table('oauth_provider_token')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        AUTH_USER_MODEL: {
            'Meta': {'object_name': User.__name__, 'db_table': "'%s'" % User._meta.db_table,},
            User._meta.pk.attname: ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'%s'" % User._meta.pk.column}),
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oauth_provider.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % AUTH_USER_MODEL, 'null': 'True', 'blank': 'True'})
        },
        'oauth_provider.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token_key': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'oauth_provider.resource': {
            'Meta': {'object_name': 'Resource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_readonly': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.TextField', [], {'max_length': '2083'})
        },
        'oauth_provider.token': {
            'Meta': {'object_name': 'Token'},
            'callback': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'null': 'True', 'blank': 'True'}),
            'callback_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth_provider.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth_provider.Resource']"}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'default': '1327884735L'}),
            'token_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tokens'", 'null': 'True', 'to': "orm['%s']" % AUTH_USER_MODEL}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['oauth_provider']

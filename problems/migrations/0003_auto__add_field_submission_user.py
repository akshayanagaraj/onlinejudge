# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.user'
        db.add_column(u'problems_submission', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.OjUser']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.user'
        db.delete_column(u'problems_submission', 'user_id')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'problems.detail': {
            'Meta': {'object_name': 'Detail'},
            'acc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accuracy': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rte': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wa': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'problems.problem': {
            'Meta': {'object_name': 'Problem'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['problems.Detail']"}),
            'explanation': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'sample_input': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'sample_output': ('django.db.models.fields.TextField', [], {'max_length': '10000'})
        },
        u'problems.submission': {
            'Meta': {'object_name': 'Submission'},
            'code': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'extime': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'prob': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['problems.Problem']"}),
            'sid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'waiting'", 'max_length': '20'}),
            'subtime': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.OjUser']"})
        },
        u'users.ojuser': {
            'Meta': {'object_name': 'OjUser', '_ormbases': [u'auth.User']},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'reg_no': ('django.db.models.fields.CharField', [], {'max_length': '23', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['problems']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.errorcode'
        db.add_column(u'problems_submission', 'errorcode',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.errorcode'
        db.delete_column(u'problems_submission', 'errorcode')


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
            'tle': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'sample_output': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'testfiles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_limit': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'problems.submission': {
            'Meta': {'object_name': 'Submission'},
            'code': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'errorcode': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
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
            'ex_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'is_loggedin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'points': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reg_no': ('django.db.models.fields.CharField', [], {'max_length': '23', 'null': 'True', 'blank': 'True'}),
            'succ_sub': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tot_sub': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['problems']
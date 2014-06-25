# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Submission'
        db.create_table(u'problems_submission', (
            ('sid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prob', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['problems.Problem'])),
            ('code', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('subtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='waiting', max_length=20)),
            ('extime', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'problems', ['Submission'])


    def backwards(self, orm):
        # Deleting model 'Submission'
        db.delete_table(u'problems_submission')


    models = {
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
            'subtime': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['problems']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Detail'
        db.create_table(u'problems_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('acc', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wa', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ce', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rte', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('accuracy', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'problems', ['Detail'])

        # Adding model 'Problem'
        db.create_table(u'problems_problem', (
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('sample_input', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('sample_output', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('explanation', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('details', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['problems.Detail'])),
        ))
        db.send_create_signal(u'problems', ['Problem'])


    def backwards(self, orm):
        # Deleting model 'Detail'
        db.delete_table(u'problems_detail')

        # Deleting model 'Problem'
        db.delete_table(u'problems_problem')


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
        }
    }

    complete_apps = ['problems']
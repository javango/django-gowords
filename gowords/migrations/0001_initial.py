# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Goword'
        db.create_table('gowords_goword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('gowords', ['Goword'])


    def backwards(self, orm):
        # Deleting model 'Goword'
        db.delete_table('gowords_goword')


    models = {
        'gowords.goword': {
            'Meta': {'object_name': 'Goword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['gowords']
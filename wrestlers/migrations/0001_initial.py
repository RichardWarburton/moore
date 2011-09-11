# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'WrestlingEntity'
        db.create_table('wrestlers_wrestlingentity', (
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('wrestlers', ['WrestlingEntity'])

        # Adding model 'Group'
        db.create_table('wrestlers_group', (
            ('wrestlingentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wrestlers.WrestlingEntity'], unique=True, primary_key=True)),
            ('group_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('wrestlers', ['Group'])

        # Adding M2M table for field members on 'Group'
        db.create_table('wrestlers_group_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['wrestlers.group'], null=False)),
            ('wrestlingentity', models.ForeignKey(orm['wrestlers.wrestlingentity'], null=False))
        ))
        db.create_unique('wrestlers_group_members', ['group_id', 'wrestlingentity_id'])

        # Adding model 'Individual'
        db.create_table('wrestlers_individual', (
            ('born_location', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('born_when', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('wrestlers', ['Individual'])

        # Adding M2M table for field trained_by on 'Individual'
        db.create_table('wrestlers_individual_trained_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_individual', models.ForeignKey(orm['wrestlers.individual'], null=False)),
            ('to_individual', models.ForeignKey(orm['wrestlers.individual'], null=False))
        ))
        db.create_unique('wrestlers_individual_trained_by', ['from_individual_id', 'to_individual_id'])

        # Adding model 'Persona'
        db.create_table('wrestlers_persona', (
            ('billed_weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('billed_height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('wrestlingentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wrestlers.WrestlingEntity'], unique=True, primary_key=True)),
            ('individual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wrestlers.Individual'])),
            ('billed_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('wrestlers', ['Persona'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'WrestlingEntity'
        db.delete_table('wrestlers_wrestlingentity')

        # Deleting model 'Group'
        db.delete_table('wrestlers_group')

        # Removing M2M table for field members on 'Group'
        db.delete_table('wrestlers_group_members')

        # Deleting model 'Individual'
        db.delete_table('wrestlers_individual')

        # Removing M2M table for field trained_by on 'Individual'
        db.delete_table('wrestlers_individual_trained_by')

        # Deleting model 'Persona'
        db.delete_table('wrestlers_persona')
    
    
    models = {
        'wrestlers.group': {
            'Meta': {'object_name': 'Group', '_ormbases': ['wrestlers.WrestlingEntity']},
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups'", 'symmetrical': 'False', 'to': "orm['wrestlers.WrestlingEntity']"}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.individual': {
            'Meta': {'object_name': 'Individual'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'born_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'born_when': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'trained_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Individual']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'wrestlers.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': ['wrestlers.WrestlingEntity']},
            'billed_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'billed_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'billed_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'individual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.Individual']"}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['wrestlers']

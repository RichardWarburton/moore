# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'CardType'
        db.create_table('matches_cardtype', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['CardType'])

        # Adding model 'CardSeries'
        db.create_table('matches_cardseries', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['CardSeries'])

        # Adding model 'Country'
        db.create_table('matches_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['Country'])

        # Adding model 'City'
        db.create_table('matches_city', (
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Country'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['City'])

        # Adding model 'Venue'
        db.create_table('matches_venue', (
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.City'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['Venue'])

        # Adding model 'Card'
        db.create_table('matches_card', (
            ('broadcast_viewership', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127, null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.CardSeries'], null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Venue'], null=True, blank=True)),
            ('card_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.CardType'])),
            ('live_attendance', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('matches', ['Card'])

        # Adding M2M table for field promotion on 'Card'
        db.create_table('matches_card_promotion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm['matches.card'], null=False)),
            ('promotion', models.ForeignKey(orm['promotions.promotion'], null=False))
        ))
        db.create_unique('matches_card_promotion', ['card_id', 'promotion_id'])

        # Adding model 'Role'
        db.create_table('matches_role', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('matches', ['Role'])

        # Adding model 'ParticipationRole'
        db.create_table('matches_participationrole', (
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Role'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Participation'])),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wrestlers.WrestlingEntity'])),
        ))
        db.send_create_signal('matches', ['ParticipationRole'])

        # Adding model 'Participation'
        db.create_table('matches_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('matches', ['Participation'])

        # Adding model 'EventType'
        db.create_table('matches_eventtype', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('matches', ['EventType'])

        # Adding model 'CardEvent'
        db.create_table('matches_cardevent', (
            ('event_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.EventType'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Card'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('matches', ['CardEvent'])

        # Adding M2M table for field participants on 'CardEvent'
        db.create_table('matches_cardevent_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cardevent', models.ForeignKey(orm['matches.cardevent'], null=False)),
            ('participation', models.ForeignKey(orm['matches.participation'], null=False))
        ))
        db.create_unique('matches_cardevent_participants', ['cardevent_id', 'participation_id'])

        # Adding model 'MatchTypeAspect'
        db.create_table('matches_matchtypeaspect', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('matches', ['MatchTypeAspect'])

        # Adding model 'MatchType'
        db.create_table('matches_matchtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['MatchType'])

        # Adding M2M table for field aspects on 'MatchType'
        db.create_table('matches_matchtype_aspects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('matchtype', models.ForeignKey(orm['matches.matchtype'], null=False)),
            ('matchtypeaspect', models.ForeignKey(orm['matches.matchtypeaspect'], null=False))
        ))
        db.create_unique('matches_matchtype_aspects', ['matchtype_id', 'matchtypeaspect_id'])

        # Adding model 'WinType'
        db.create_table('matches_wintype', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('matches', ['WinType'])

        # Adding model 'Match'
        db.create_table('matches_match', (
            ('win_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.WinType'], null=True, blank=True)),
            ('match_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.MatchType'])),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='title_matches', null=True, to=orm['promotions.Title'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='won_matches', null=True, to=orm['wrestlers.WrestlingEntity'])),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('cardevent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['matches.CardEvent'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('matches', ['Match'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'CardType'
        db.delete_table('matches_cardtype')

        # Deleting model 'CardSeries'
        db.delete_table('matches_cardseries')

        # Deleting model 'Country'
        db.delete_table('matches_country')

        # Deleting model 'City'
        db.delete_table('matches_city')

        # Deleting model 'Venue'
        db.delete_table('matches_venue')

        # Deleting model 'Card'
        db.delete_table('matches_card')

        # Removing M2M table for field promotion on 'Card'
        db.delete_table('matches_card_promotion')

        # Deleting model 'Role'
        db.delete_table('matches_role')

        # Deleting model 'ParticipationRole'
        db.delete_table('matches_participationrole')

        # Deleting model 'Participation'
        db.delete_table('matches_participation')

        # Deleting model 'EventType'
        db.delete_table('matches_eventtype')

        # Deleting model 'CardEvent'
        db.delete_table('matches_cardevent')

        # Removing M2M table for field participants on 'CardEvent'
        db.delete_table('matches_cardevent_participants')

        # Deleting model 'MatchTypeAspect'
        db.delete_table('matches_matchtypeaspect')

        # Deleting model 'MatchType'
        db.delete_table('matches_matchtype')

        # Removing M2M table for field aspects on 'MatchType'
        db.delete_table('matches_matchtype_aspects')

        # Deleting model 'WinType'
        db.delete_table('matches_wintype')

        # Deleting model 'Match'
        db.delete_table('matches_match')
    
    
    models = {
        'matches.card': {
            'Meta': {'object_name': 'Card'},
            'broadcast_viewership': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'card_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.CardType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live_attendance': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['promotions.Promotion']", 'symmetrical': 'False'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.CardSeries']", 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Venue']", 'null': 'True', 'blank': 'True'})
        },
        'matches.cardevent': {
            'Meta': {'object_name': 'CardEvent'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Card']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.EventType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['matches.Participation']", 'symmetrical': 'False'})
        },
        'matches.cardseries': {
            'Meta': {'object_name': 'CardSeries'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.cardtype': {
            'Meta': {'object_name': 'CardType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'matches.match': {
            'Meta': {'object_name': 'Match', '_ormbases': ['matches.CardEvent']},
            'cardevent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['matches.CardEvent']", 'unique': 'True', 'primary_key': 'True'}),
            'match_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.MatchType']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'title_matches'", 'null': 'True', 'to': "orm['promotions.Title']"}),
            'win_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.WinType']", 'null': 'True', 'blank': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'won_matches'", 'null': 'True', 'to': "orm['wrestlers.WrestlingEntity']"})
        },
        'matches.matchtype': {
            'Meta': {'object_name': 'MatchType'},
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['matches.MatchTypeAspect']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'matches.matchtypeaspect': {
            'Meta': {'object_name': 'MatchTypeAspect'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'matches.participation': {
            'Meta': {'object_name': 'Participation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'through': "orm['matches.ParticipationRole']", 'symmetrical': 'False'})
        },
        'matches.participationrole': {
            'Meta': {'object_name': 'ParticipationRole'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.WrestlingEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Participation']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Role']"})
        },
        'matches.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'matches.venue': {
            'Meta': {'object_name': 'Venue'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.wintype': {
            'Meta': {'object_name': 'WinType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.title': {
            'Meta': {'object_name': 'Title'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['matches']

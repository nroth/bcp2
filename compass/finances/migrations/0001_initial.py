# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'finances_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'finances', ['Campaign'])

        # Adding model 'Individual'
        db.create_table(u'finances_individual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('allow_future_contact', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('point_person', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
        ))
        db.send_create_signal(u'finances', ['Individual'])

        # Adding model 'Business'
        db.create_table(u'finances_business', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('allow_future_contact', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
        ))
        db.send_create_signal(u'finances', ['Business'])

        # Adding model 'BusinessDonation'
        db.create_table(u'finances_businessdonation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Business'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('outcome', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'finances', ['BusinessDonation'])

        # Adding model 'IndividualDonation'
        db.create_table(u'finances_individualdonation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Individual'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('matching_funds', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('matching_source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=2047, blank=True)),
            ('referrer', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('confirmation_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fund_number', self.gf('django.db.models.fields.CharField')(max_length=31, null=True, blank=True)),
            ('fund_description', self.gf('django.db.models.fields.CharField')(max_length=31, null=True, blank=True)),
        ))
        db.send_create_signal(u'finances', ['IndividualDonation'])

        # Adding model 'IndividualAsk'
        db.create_table(u'finances_individualask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Campaign'], blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
        ))
        db.send_create_signal(u'finances', ['IndividualAsk'])

        # Adding M2M table for field contacts on 'IndividualAsk'
        db.create_table(u'finances_individualask_contacts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('individualask', models.ForeignKey(orm[u'finances.individualask'], null=False)),
            ('individual', models.ForeignKey(orm[u'finances.individual'], null=False))
        ))
        db.create_unique(u'finances_individualask_contacts', ['individualask_id', 'individual_id'])

        # Adding model 'BusinessAsk'
        db.create_table(u'finances_businessask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Campaign'], blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
        ))
        db.send_create_signal(u'finances', ['BusinessAsk'])

        # Adding M2M table for field contacts on 'BusinessAsk'
        db.create_table(u'finances_businessask_contacts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('businessask', models.ForeignKey(orm[u'finances.businessask'], null=False)),
            ('business', models.ForeignKey(orm[u'finances.business'], null=False))
        ))
        db.create_unique(u'finances_businessask_contacts', ['businessask_id', 'business_id'])


    def backwards(self, orm):
        # Deleting model 'Campaign'
        db.delete_table(u'finances_campaign')

        # Deleting model 'Individual'
        db.delete_table(u'finances_individual')

        # Deleting model 'Business'
        db.delete_table(u'finances_business')

        # Deleting model 'BusinessDonation'
        db.delete_table(u'finances_businessdonation')

        # Deleting model 'IndividualDonation'
        db.delete_table(u'finances_individualdonation')

        # Deleting model 'IndividualAsk'
        db.delete_table(u'finances_individualask')

        # Removing M2M table for field contacts on 'IndividualAsk'
        db.delete_table('finances_individualask_contacts')

        # Deleting model 'BusinessAsk'
        db.delete_table(u'finances_businessask')

        # Removing M2M table for field contacts on 'BusinessAsk'
        db.delete_table('finances_businessask_contacts')


    models = {
        u'finances.business': {
            'Meta': {'object_name': 'Business'},
            'allow_future_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'finances.businessask': {
            'Meta': {'object_name': 'BusinessAsk'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finances.Campaign']", 'blank': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finances.Business']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'})
        },
        u'finances.businessdonation': {
            'Meta': {'object_name': 'BusinessDonation'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finances.Business']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outcome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'finances.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'finances.individual': {
            'Meta': {'object_name': 'Individual'},
            'allow_future_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'point_person': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'finances.individualask': {
            'Meta': {'object_name': 'IndividualAsk'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finances.Campaign']", 'blank': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finances.Individual']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'})
        },
        u'finances.individualdonation': {
            'Meta': {'object_name': 'IndividualDonation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2047', 'blank': 'True'}),
            'confirmation_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finances.Individual']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'fund_description': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'fund_number': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matching_funds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'matching_source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['finances']
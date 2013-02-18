# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table(u'people_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1023, blank=True)),
        ))
        db.send_create_signal(u'people', ['Role'])

        # Adding model 'Person'
        db.create_table(u'people_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('public_profile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_compass_contact', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('allow_other_contact', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Person'])

        # Adding unique constraint on 'Person', fields ['content_type', 'object_id']
        db.create_unique(u'people_person', ['content_type_id', 'object_id'])

        # Adding model 'Undergrad'
        db.create_table(u'people_undergrad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ethnic_groups', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('entered_cal_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('joined_compass_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('graduation_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('undergrad_research', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('graduate_school', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('household_income', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('parental_degrees', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('first_generation', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Undergrad'])

        # Adding model 'Transfer'
        db.create_table(u'people_transfer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ethnic_groups', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('entered_cal_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('joined_compass_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('graduation_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('undergrad_research', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('graduate_school', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('previous_institution', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'people', ['Transfer'])

        # Adding model 'GradStudent'
        db.create_table(u'people_gradstudent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ethnic_groups', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=2047, blank=True)),
            ('entered_cal_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('joined_compass_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('ma_graduation_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('phd_graduation_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'people', ['GradStudent'])

        # Adding model 'Postdoc'
        db.create_table(u'people_postdoc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'people', ['Postdoc'])

        # Adding model 'Term'
        db.create_table(u'people_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Role'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'people', ['Term'])

        # Adding model 'CompassUser'
        db.create_table(u'people_compassuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.Person'], unique=True, null=True, blank=True)),
            ('has_requested_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'people', ['CompassUser'])

        # Adding M2M table for field groups on 'CompassUser'
        db.create_table(u'people_compassuser_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compassuser', models.ForeignKey(orm[u'people.compassuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'people_compassuser_groups', ['compassuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CompassUser'
        db.create_table(u'people_compassuser_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compassuser', models.ForeignKey(orm[u'people.compassuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'people_compassuser_user_permissions', ['compassuser_id', 'permission_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Person', fields ['content_type', 'object_id']
        db.delete_unique(u'people_person', ['content_type_id', 'object_id'])

        # Deleting model 'Role'
        db.delete_table(u'people_role')

        # Deleting model 'Person'
        db.delete_table(u'people_person')

        # Deleting model 'Undergrad'
        db.delete_table(u'people_undergrad')

        # Deleting model 'Transfer'
        db.delete_table(u'people_transfer')

        # Deleting model 'GradStudent'
        db.delete_table(u'people_gradstudent')

        # Deleting model 'Postdoc'
        db.delete_table(u'people_postdoc')

        # Deleting model 'Term'
        db.delete_table(u'people_term')

        # Deleting model 'CompassUser'
        db.delete_table(u'people_compassuser')

        # Removing M2M table for field groups on 'CompassUser'
        db.delete_table('people_compassuser_groups')

        # Removing M2M table for field user_permissions on 'CompassUser'
        db.delete_table('people_compassuser_user_permissions')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.compassuser': {
            'Meta': {'object_name': 'CompassUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'has_requested_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['people.Person']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'people.gradstudent': {
            'Meta': {'object_name': 'GradStudent'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'entered_cal_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ethnic_groups': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined_compass_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ma_graduation_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'phd_graduation_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'people.person': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Person'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_compass_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_other_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'public_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['people.Role']", 'through': u"orm['people.Term']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'people.postdoc': {
            'Meta': {'object_name': 'Postdoc'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1023', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'people.term': {
            'Meta': {'object_name': 'Term'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Role']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'people.transfer': {
            'Meta': {'object_name': 'Transfer'},
            'entered_cal_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ethnic_groups': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'graduate_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'graduation_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined_compass_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'previous_institution': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'undergrad_research': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'people.undergrad': {
            'Meta': {'object_name': 'Undergrad'},
            'entered_cal_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ethnic_groups': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'first_generation': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'graduate_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'graduation_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'household_income': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined_compass_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '2047', 'blank': 'True'}),
            'parental_degrees': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'undergrad_research': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['people']
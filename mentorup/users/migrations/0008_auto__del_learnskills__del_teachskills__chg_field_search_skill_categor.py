# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LearnSkills'
        db.delete_table(u'users_learnskills')

        # Deleting model 'TeachSkills'
        db.delete_table(u'users_teachskills')


        # Changing field 'Search.skill_categories'
        db.alter_column(u'users_search', 'skill_categories_id', self.gf('select2.fields.ForeignKey')(to=orm['users.Skills'], search_field='name'))
        # Adding field 'Skills.name'
        db.add_column(u'users_skills', 'name',
                      self.gf('django.db.models.fields.CharField')(default='BadValueDeleteMe', max_length=50),
                      keep_default=False)

        # Deleting field 'User.learn'
        db.delete_column(u'users_user', 'learn_id')

        # Deleting field 'User.teach'
        db.delete_column(u'users_user', 'teach_id')


    def backwards(self, orm):
        # Adding model 'LearnSkills'
        db.create_table(u'users_learnskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'users', ['LearnSkills'])

        # Adding model 'TeachSkills'
        db.create_table(u'users_teachskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'users', ['TeachSkills'])


        # Changing field 'Search.skill_categories'
        db.alter_column(u'users_search', 'skill_categories_id', self.gf('select2.fields.ForeignKey')(to=orm['users.Skills'], search_field='tags'))
        # Deleting field 'Skills.name'
        db.delete_column(u'users_skills', 'name')

        # Adding field 'User.learn'
        db.add_column(u'users_user', 'learn',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.LearnSkills'], unique=True, null=True),
                      keep_default=False)

        # Adding field 'User.teach'
        db.add_column(u'users_user', 'teach',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.TeachSkills'], unique=True, null=True),
                      keep_default=False)


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
        u'users.search': {
            'Meta': {'object_name': 'Search'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill_categories': ('select2.fields.ForeignKey', [], {'to': u"orm['users.Skills']", 'search_field': "'name'"})
        },
        u'users.skills': {
            'Meta': {'object_name': 'Skills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'short_bio': ('django.db.models.fields.TextField', [], {}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['users']
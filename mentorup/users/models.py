# -*- coding: utf-8 -*-
# Import chosenforms for pretty search forms
from chosen import forms as chosenforms
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models and forms library
from django.db import models
from django.db.models.signals import post_save
from django import forms

# Import tags for searching
from taggit.models import Tag
from taggit.models import TagBase
from taggit.managers import TaggableManager

from django.utils.translation import ugettext_lazy as _

# Create seperate classes for each tag type that will be a foreign key reference from User
class TeachSkills(models.Model):
    skills = TaggableManager()

class LearnSkills(models.Model):
    skills = TaggableManager()

# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

    teach = models.ForeignKey(TeachSkills, null=True)
    learn = models.ForeignKey(LearnSkills, null=True)
    short_bio = models.TextField()
    location = models.CharField(max_length=50)

    def save_skill_teach(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.teach.skills.add(tag_skill)
        self.teach.skills.add(tag)
        return tag + " tag saved."   

    def save_skill_learn(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.learn.skills.add(tag_skill)
        self.learn.skills.add(tag)
        return tag + " tag saved."   

    def get_skill_teach(self):
        return self.teach.skills.all()

    def get_skill_learn(self):
        return self.learn.skills.all()


def create_skill_association(sender, instance, created, **kwargs):
    if created:
        instance.teach = TeachSkills()
        instance.teach.save()
        instance.learn = LearnSkills()
        instance.learn.save()


post_save.connect(create_skill_association, sender=User)
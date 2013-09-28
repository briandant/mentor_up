# -*- coding: utf-8 -*-
# Import chosenforms for pretty search forms
from chosen import forms as chosenforms
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models and forms library
from django.db import models
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

    short_bio = models.TextField()
    location = models.CharField(max_length=50)
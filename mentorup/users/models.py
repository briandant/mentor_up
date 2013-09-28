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

    # Related tag models
    teach = models.ForeignKey(TeachSkills, null=True)
    learn = models.ForeignKey(LearnSkills, null=True)
    short_bio = models.TextField()
    location = models.CharField(max_length=50)

    # Method for saving a selected skill that a user wants to teach
    # Expected format is user.save_skill_teach("Python", "Beginner")
    def save_skill_teach(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.teach.skills.add(tag_skill)
        self.teach.skills.add(tag)
        self.save()
        return tag + " tag saved."   

    # Method for saving a selected skill that a user wants to learn
    # Expected format is user.save_skill_learn("Django", "Expert")
    def save_skill_learn(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.learn.skills.add(tag_skill)
        self.learn.skills.add(tag)
        self.save()
        return tag + " tag saved."   

    # Returns all tags, skills that a user can teach
    def get_skill_teach(self):
        return self.teach.skills.all()

    # Returns all tags, skills that a user wishes to learn
    def get_skill_learn(self):
        return self.learn.skills.all()

# post_save method to associate tags with user upon user creation.
def create_skill_association(sender, instance, created, **kwargs):
    if created:
        teach = TeachSkills()
        teach.save()
        instance.teach = teach
        learn = LearnSkills()
        learn.save()
        instance.learn = learn
        instance.save()


post_save.connect(create_skill_association, sender=User)

class Search(models.Model):

    @classmethod
    def tag_user(self, tag):
        return User.objects.filter(tags__name__in=tag).distinct()
# Note: access the skills -> user.skills.filter(endswith="Expert")

class Skills(models.Model):

    tags = TaggableManager()

    # Call this method when initializing the available tags in the DB.
    # It can be called safely multiple times without issue, as django-taggit checks against duplicates
    @classmethod
    def generate_tags(cls):
        base_tags = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Javascript", "Node.js", "Angular", "Backbone", "Scala", "PHP", "Java", "HTML5", "CSS3", "Jquery"]
        skill_level_tags = ["No Experience", "Beginner", "Intermediate", "Expert"]
        manager = Skills.objects.get_or_create(pk=1)[0]
        for tag in base_tags:
            for skill_tag in skill_level_tags:
                tag_skill = "%s %s" %(tag, skill_tag)
                tag = "%s" %(tag)
                manager.tags.add(tag_skill)
                manager.tags.add(tag)

    # Create a single tag with this method, if you specify a skill level ( which you should )
    # It will also create the base tag.  I.E. Skills.create_tag("Python", "Expert")
    # Will create the tag "Python" as well as the tag "Python Expert"
    @classmethod
    def create_tag(cls, tag, skill_level=None):
        manager = Skills.objects.get_or_create(pk=1)[0]
        if not skill_level:
            tag = "%s" %(tag)
            manager.tags.add(tag)
        else:
            tag_skill = "%s %s" %(tag, skill_level)
            tag = "%s" %(tag)
            manager.tags.add(tag_skill)
            manager.tags.add(tag)          


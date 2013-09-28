# -*- coding: utf-8 -*-
# Import chosenforms for pretty search forms
from chosen import forms as chosenforms
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models and forms library
from django.db import models
from django.db.models.signals import post_save
from django import forms
from django.db.models import Q

from django.utils.translation import ugettext_lazy as _

# import select 2 fields and forms for skill tag searching
import select2.fields
import select2.models

class Skills(models.Model):
    """
    Model for storing skills and associating them with a user
    """
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    teach = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name + " Teach: " + str(self.teach)

    @classmethod
    def generate_skills(cls):
        """
        Call this method when initializing the available tags in the DB.
        It can be called safely multiple times without issue, as it checks against duplicates
        """
        base_skills = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Javascript", "Node.js", "Angular", "Backbone", "Scala", "PHP", "Java", "HTML5", "CSS3", "Jquery"]
        skill_levels = ["No Experience", "Beginner", "Intermediate", "Expert"]
        for skill in base_skills:
            for skill_level in skill_levels:
                tag_skill = "%s %s" %(skill, skill_level)
                tag = "%s" %(skill)
                Skills.objects.get_or_create(name=tag, teach=False)
                Skills.objects.get_or_create(name=tag_skill, teach=False)
                Skills.objects.get_or_create(name=tag, teach=True)
                Skills.objects.get_or_create(name=tag_skill, teach=True)

    @classmethod
    def create_skill(cls, skill, skill_level=None):
        """
        Create a single tag with this method, if you specify a skill level ( which you should )
        It will also create the base skill.  I.E. Skills.create_skill("Python", "Expert")
        will create the skill "Python" as well as the skill "Python Expert"
        """
        if skill_level:
            tag_skill = "%s %s" %(skill, skill_level)
            tag = "%s" %(skill)  
            Skills.objects.get_or_create(name=tag, teach=False)
            Skills.objects.get_or_create(name=tag_skill, teach=False)
            Skills.objects.get_or_create(name=tag, teach=True)
            Skills.objects.get_or_create(name=tag_skill, teach=True)
        else:
            tag = "%s" %(skill)
            Skills.objects.get_or_create(name=tag, teach=False)
            Skills.objects.get_or_create(name=tag, teach=True)

    @classmethod
    def create_skills_levels(cls, skills, skill_levels=["No Experience", "Beginner", "Intermediate", "Expert"]):
        """
        Create a skill for each skill level, and the base skill.
        Pass in multiple skills to add more than one ( expects an array either way ).
        I.E. Skills.create_skill_levels("Python")
        Will create the skills "Python", "Python No Experience", "Python Beginner", "Python Intermediate", "Python Expert"
        Specify an array for skill_levels to input custom skill levels.
        Checks for duplicates, and will only save unique values.
        """
        for skill in skills:
            for skill_level in skill_levels:
                tag_skill = "%s %s" %(skill, skill_level)
                tag = "%s" %(skill)
                Skills.objects.get_or_create(name=tag, teach=False)
                Skills.objects.get_or_create(name=tag_skill, teach=False)
                Skills.objects.get_or_create(name=tag, teach=True)
                Skills.objects.get_or_create(name=tag_skill, teach=True)

# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

    skills = models.ManyToManyField(Skills, null=True)
    short_bio = models.TextField()
    location = models.CharField(max_length=50)


class Search(models.Model):
    """
    Model for hooking up available skill classes with ajax
    search autocomplete requests.
    """
    skill_categories = select2.fields.ForeignKey(Skills,
        limit_choices_to=models.Q(active=True),
        ajax=True,
        search_field='name',
        case_sensitive=False,
        overlay="Choose a Skill Tag to Search by",
        js_options={},
        )








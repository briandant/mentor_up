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

from allauth.socialaccount.models import SocialAccount

from django.utils.translation import ugettext_lazy as _

# import select 2 fields and forms for skill tag searching
import select2.fields
import select2.models


class Skills(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    teach = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name + " Teach: " + str(self.teach)


    # Call this method when initializing the available tags in the DB.
    # It can be called safely multiple times without issue, as django-taggit checks against duplicates
    @classmethod
    def generate_skills(cls):
        base_tags = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Javascript", "Node.js", "Angular", "Backbone", "Scala", "PHP", "Java", "HTML5", "CSS3", "Jquery"]
        skill_level_tags = ["No Experience", "Beginner", "Intermediate", "Expert"]
        for tag in base_tags:
            for skill_tag in skill_level_tags:
                tag_skill = "%s %s" %(tag, skill_tag)
                tag = "%s" %(tag)
                Skills.objects.get_or_create(name=tag, teach=False)
                Skills.objects.get_or_create(name=tag_skill, teach=False)
                Skills.objects.get_or_create(name=tag, teach=True)
                Skills.objects.get_or_create(name=tag_skill, teach=True)

    # Create a single tag with this method, if you specify a skill level ( which you should )
    # It will also create the base tag.  I.E. Skills.create_tag("Python", "Expert")
    # Will create the tag "Python" as well as the tag "Python Expert"
    @classmethod
    def create_skill(cls, tag, skill_level=None, teach=False):
        if not skill_level:
            tag = "%s" %(tag)
            Skills.objects.get_or_create(name=tag, teach=teach)
        else:
            tag_skill = "%s %s" %(tag, skill_level)
            tag = "%s" %(tag)  
            Skills.objects.get_or_create(name=tag, teach=teach)
            Skills.objects.get_or_create(name=tag_skill, teach=teach)


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

    skills = models.ManyToManyField(Skills, null=True)
    short_bio = models.TextField()
    location = models.CharField(max_length=50)

    def github_profile_url(self): 
        """ 
        Given a user, return the profile URL of their Github account
        """
        accounts = SocialAccount.objects.filter(user=self)

        for account in accounts:
            if account.provider == 'github':
                return account.get_profile_url()
            else:
                return None


class Search(models.Model):
    skill_categories = select2.fields.ForeignKey(Skills,
        limit_choices_to=models.Q(active=True),
        ajax=True,
        search_field='name',
        case_sensitive=False,
        overlay="Choose a Skill Tag to Search by",
        js_options={},
    )


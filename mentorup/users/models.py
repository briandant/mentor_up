# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models and forms library
from django.db import models
from django.db.models.signals import post_save
from django import forms
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from allauth.socialaccount.models import SocialAccount

# import select 2 fields and forms for skill tag searching
import select2.fields
import select2.models


LOCATIONS = (
        ('boston', 'Boston, MA'),
        ('newyork', 'New York, NY'),
        ('sanfrancisco', 'San Francisco, CA'),
        ('washingtondc', 'Washington, DC'),
        ('seattle', 'Seattle, WA'),
        ('austin', 'Austin, TX'),
        ('portland', 'Portland, OR'),
        ('minneapolis', 'Minneapolis, MN'),
        ('chicago', 'Chicago, IL'),
        ('boulder', 'Boulder, CO'),
        ('other', 'Other')
    )


class Skill(models.Model):
    """
    Model for storing skills and associating them with a user
    """
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return unicode(self.username)

    skills_to_teach = models.ManyToManyField(Skill, related_name='skills_to_teach')
    skills_to_learn = models.ManyToManyField(Skill, related_name='skills_to_learn')

    short_bio = models.TextField()
    location = models.CharField(max_length=50, choices=LOCATIONS, default="boston")

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

    def display_location(self):
        """
        Given a location value, return the humanized location
        """
        locations = dict(LOCATIONS)
        return locations[self.location]


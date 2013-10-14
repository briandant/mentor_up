# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models and forms library
from django.db import models
from allauth.socialaccount.models import SocialAccount


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

    skills_to_teach = models.ManyToManyField(Skill, related_name='skills_to_teach', blank=True)
    skills_to_learn = models.ManyToManyField(Skill, related_name='skills_to_learn', blank=True)

    available_to_teach = models.BooleanField(default=False)
    availability_description = models.TextField()

    short_bio = models.TextField()
    location = models.CharField(max_length=50, choices=sorted(LOCATIONS), default="boston")

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

    def display_skills_to_teach(self):
        """
        Given a user, return a comma separated list of
        skills they want to teach
        """
        skills = self.skills_to_teach.all()
        return ", ".join([str(skill) for skill in skills])

    def display_skills_to_learn(self):
        """
        Given a user, return a comma separated list of
        skills they want to learn
        """
        skills = self.skills_to_learn.all()
        return ", ".join([str(skill) for skill in skills])

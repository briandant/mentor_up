# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# query imports
from django.db.models import Q

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm, MemberSearchForm

# Import the customized User model
from .models import User, Skill

import json


class UserDetailView(DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username})


@login_required()
def user_update_view(request, template='users/user_form.html'):
    instance = User.objects.get(username=request.user.username)

    if request.method == 'POST':

        form = UserForm(request.POST, instance=instance)
        if form.is_valid():

            form.save()

            success_url = reverse(
                "users:detail",
                kwargs={"username": request.user.username})

            return redirect(success_url)

    else:  # Get request
        form = UserForm(instance=instance)

    return render(
        request,
        template,
        {'form': form}
    )


def user_search_view(request):

    print request.GET
    print request.GET.get('skills_to_search')
    # skills = request.GET.get('skills_to_search', None)

    # Brian
    # skill_objects = Skill.objects.filter(

    # User.objects.filter(skills_to_teach__=skills_to_learn_set.all())

    # if skills:
    #     int_skills = [int(skill) for skill in skills]
    #     matching_users = User.objects.filter(skills_to_teach__id__in=[int_skills])[:20]

    # matching_users = User.objects.all()
    # for matching_user in matching_users:

    # Chris
    # queryz = User.objects.all().filter(Q(skills_to_teach__name="Python") | Q(skills_to_teach__name="Django")).distinct()
    # print queryz

    skill_values = request.GET.get('skills_to_search')

    # Search for users with the skills 'Django' and 'Ruby'
    skill_primary_keys = [5, 4]

    # Turn list of values into list of Q objects
    queries = [Q(skills_to_teach__pk=value) for value in skill_primary_keys]

    # Initialize Query
    query = Q()

    # Or the Q object with the ones remaining in the list
    for item in queries:
        query |= item

    # Query the model for all users that have the skills_to_teach we're searching for
    user_list = User.objects.filter(query).distinct()
    print user_list

    return HttpResponseRedirect(reverse('users:list'))


class UserListView(ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    # Template select bar for pages not implemented yet
    # def get_paginate_by(self, queryset):
    #     self.paginate_by = 20
    #     return self.paginate_by

    def get_queryset(self):
        """
        Get the list of items for this view. This must be an iterable, and may
        be a queryset (in which qs-specific behavior will be enabled).
        """

        if self.queryset is not None:
            queryset = self.queryset

            if hasattr(queryset, '_clone'):
                queryset = queryset._clone()

        elif self.model is not None:
            queryset = self.model._default_manager.all()

        else:
            raise ImproperlyConfigured("'%s' must define 'queryset' or 'model'"
                                       % self.__class__.__name__)

        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['search_form'] = MemberSearchForm()
        return context

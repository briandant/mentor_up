# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView, RedirectView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# query imports
from django.db.models import Q

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm, MemberSearchForm

# Import the customized User model
from .models import User, Skill


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
    pass


class UserListView(ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_queryset(self):
        """
        Get the list of items for this view. This must be an iterable, and may
        be a queryset (in which qs-specific behavior will be enabled).
        """
        queryset = self.model.objects.all()
        search_skills = self.request.GET.getlist('skills_to_search', None)
        search_locations = self.request.GET.getlist('locations_to_search', None)

        if not self.request.GET and self.request.user.is_active:
            search_skills = self.request.user.skills_to_learn.all()
            search_locations = [self.request.user.location]

        if search_skills and not search_locations:
            # If there is no location provided, just
            # query the model for all users that have the skills_to_teach we're searching for
            queryset = self.model.objects.filter(skills_to_teach__pk__in=search_skills)

        elif search_locations and not search_skills:
            # If there is no location provided, just
            # query the model for all users that live in the location(s) we're searching for
            queryset = self.model.objects.filter(location__in=search_locations)

        elif search_locations and search_skills:
            # If the location and skills to search are provided,
            # query the model for all users that live in the location(s) and have the skill(s) 
            queryset = self.model.objects.filter(location__in=search_locations).filter(skills_to_teach__pk__in=search_skills)

        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['search_form'] = MemberSearchForm()
        context['hide_navbar_search'] = True
        search_skill_ids = self.request.GET.getlist('skills_to_search', None)
        search_skill_objects = Skill.objects.filter(id__in=search_skill_ids)
        context['previously_selected_search_skills'] = dict((skill.id, str(skill.name)) for skill in search_skill_objects)
        return context

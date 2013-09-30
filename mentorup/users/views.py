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
from django.http import HttpResponse

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

#    skills = request.GET.get('skills_to_search', None)
#    skill_objects = Skill.objects.filter(
#
#    User.objects.filter(skills_to_teach__=skills_to_learn_set.all())
#
#    if skills:
#        int_skills = [int(skill) for skill in skills]
#        matching_users = User.objects.filter(skills_to_teach__id__in=[int_skills])[:20]
#
#    matching_users = User.objects.all()
#    for matching_user in matching_users:
#
#        if
#
#    return HttpResponse(matching_users)


class UserListView(ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['search_form'] = MemberSearchForm()
        return context

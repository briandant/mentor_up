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

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm

# Import the customized User model
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
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
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            form.save()

            success_url = reverse(
                "users:detail",
                kwargs={"username": request.user.username})

            return redirect(success_url)

        return render(
            request,
            template,
            {'form': form}
        )

    else:  # Get request
        form = UserForm()

        return render(
            request,
            template,
            {'form': form}
        )


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

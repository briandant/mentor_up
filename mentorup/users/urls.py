# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w\-_]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.user_update_view,
        name='update'
    ),

    # URL pattern for the UserSearchView
    url(
        regex=r'^~search/$',
        view=views.user_search_view,
        name='search'
    ),

)

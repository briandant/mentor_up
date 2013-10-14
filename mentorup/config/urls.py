# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

# Import postman URL requirements for customization
from django.views.generic.base import RedirectView

from postman import OPTIONS
from postman.views import (InboxView, SentView, ArchivesView, TrashView,
        WriteView, ReplyView, MessageView, ConversationView,
        ArchiveView, DeleteView, UndeleteView)

from users.views import sender_profile_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url="users/"),
        name="home"),
    url(r'^about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    # url(r'^messages/', include('postman.urls')),

    # URL pattern for select2's AJAX Support
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('postman.views',
    url(r'^messages/inbox/(?:(?P<option>'+OPTIONS+')/)?$', InboxView.as_view(), name='postman_inbox'),
    url(r'^messages/sent/(?:(?P<option>'+OPTIONS+')/)?$', SentView.as_view(), name='postman_sent'),
    url(r'^messages/archives/(?:(?P<option>'+OPTIONS+')/)?$', ArchivesView.as_view(), name='postman_archives'),
    url(r'^messages/trash/(?:(?P<option>'+OPTIONS+')/)?$', TrashView.as_view(), name='postman_trash'),
    url(r'^messages/write/(?:(?P<recipients>[\w.@+-:]+)/)?$', WriteView.as_view(exchange_filter=sender_profile_required), name='postman_write'),
    url(r'^messages/reply/(?P<message_id>[\d]+)/$', ReplyView.as_view(), name='postman_reply'),
    url(r'^messages/view/(?P<message_id>[\d]+)/$', MessageView.as_view(), name='postman_view'),
    url(r'^messages/view/t/(?P<thread_id>[\d]+)/$', ConversationView.as_view(), name='postman_view_conversation'),
    url(r'^messages/archive/$', ArchiveView.as_view(), name='postman_archive'),
    url(r'^messages/delete/$', DeleteView.as_view(), name='postman_delete'),
    url(r'^messages/undelete/$', UndeleteView.as_view(), name='postman_undelete'),
    (r'^$', RedirectView.as_view(url='inbox/')),
)
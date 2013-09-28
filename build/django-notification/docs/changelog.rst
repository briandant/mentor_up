.. _changelog:

ChangeLog
=========

BI = backward incompatible change

1.1.1
-----

* fixed a deprecation warning


1.1
---

* added Russian locale
* added travis integration for tests/lints
* added created_notice_type wrapper
* cleaned up some small bugs identified by pylint


1.0
---

* removed unused `message.py` module
* removed `captureas` templatetag
* added `notice_settings.html` template
* other minor fixes and tweaks, mostly to code style

0.3
---

* pluggable backends

0.2.0
-----

* BI: renamed Notice.user to Notice.recipient
* BI: renamed {{ user }} context variable in notification templates to
  {{ recipient }}
* BI: added nullable Notice.sender and modified send_now and queue to take
  an optional sender
* added received and sent methods taking a User instance to Notice.objects
* New default behavior: single notice view now marks unseen notices as seen
* no longer optionally depend on mailer; use django.core.mail.send_mail and
  we now encourge use of Django 1.2+ for mailer support
* notifications are not sent to inactive users
* users which do not exist when sending notification are now ignored
* BI: split settings part of notices view to its own view notice_settings

0.1.5
-----

* added support for DEFAULT_HTTP_PROTOCOL allowing https absolute URLs

Install
=========

Create a virtualenv
-------------------

To get Mentor Up running locally, you first need to make a virtualenv. 
If you have virtualenvwrapper installed, then you can just type::

	$ mkvirtualenv mentorup

Otherwise, you can install virtualenv with::

	$ pip install virtualenv

And create the virtualenv with::

	$ virtualenv mentorup

Activate the virtualenv::

	$ source mentorup/bin/activate

Configure the Mentor Up project
-------------------------------

Install the requirements::

	$ cd /path/to/mentorup/repo
	(mentorup)$ pip install -r requirements/local.txt
	...

Sync and migrate the database and start the server::

	$ python mentorup/manage.py syncdb
	$ python mentorup/manage.py migrate
	$ python mentorup/manage.py runserver

NOTE: if you're on a Mac, the easiest way to create a 
PostgreSQL database is to install Postgres.app_ and pgAdmin3_.

.. _pgAdmin3: http://www.pgadmin.org/download/macosx.php

.. _Postgres.app: http://postgresapp.com
	
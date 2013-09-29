Mentor UP
==============================

Django Dash 2013 project exploring ways to connect mentors and mentees learning to code.


LICENSE: BSD

For instructions on how to deploy this project to Heroku, look in ```docs/deploy.rst```.

Using Sass
----------

We're using Sass for stylesheets in a very simple way.  You've just gotta understand variables and CSS selector inheritance.  We're not doing anything crazy, and all valid CSS is Sass compliant.

.. codeblock::

	gem install compass
	cd mentorup/static
	compass watch

Compass will now watch the changes you make to any ```sass/file.scss``` files, and generating a .css that our html templates are reading.


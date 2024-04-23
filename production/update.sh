#!/bin/sh
/usr/bin/git pull

# collectstatic?
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput

# reload gunicorn
touch /srv/www/rubens_blog/rubens_blog/rubens_blog/wsgi.py


# postgresql       manage.py migrate?
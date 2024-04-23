#!/bin/sh
/usr/bin/git pull

# collectstatic?
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput

# restart gunicorn
systemctl restart gunicorn

# postgresql       manage.py migrate?
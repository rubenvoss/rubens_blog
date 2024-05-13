#!/bin/sh
echo "export ENV_NAME=production"
export ENV_NAME=production

echo "/usr/bin/git pull"
/usr/bin/git pull

# collect static files
echo "/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput"
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput

# install new reqs
echo "/srv/www/rubens_blog/venv/bin/pip install -r /srv/www/rubens_blog/requirements.txt | grep -v 'Requirement already satisfied:'"
/srv/www/rubens_blog/venv/bin/pip install -r /srv/www/rubens_blog/requirements.txt | grep -v 'Requirement already satisfied:'

# migrate db
echo "/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py migrate"
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py migrate

# restart gunicorn
echo "systemctl reload gunicorn"
systemctl reload gunicorn

# restart webhook
systemctl reload webhook


#!/bin/sh
echo "[EXECUTING COMMAND] export ENV_NAME=production"
export ENV_NAME=production

echo "[EXECUTING COMMAND] /usr/bin/git pull"
/usr/bin/git pull

# collect static files
echo "[EXECUTING COMMAND] /srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput"
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py collectstatic --noinput

# install new reqs
echo "[EXECUTING COMMAND] /srv/www/rubens_blog/venv/bin/pip install -r /srv/www/rubens_blog/requirements.txt | grep -v 'Requirement already satisfied:'"
/srv/www/rubens_blog/venv/bin/pip install -r /srv/www/rubens_blog/requirements.txt | grep -v 'Requirement already satisfied:'

# migrate db
echo "[EXECUTING COMMAND] /srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py migrate"
/srv/www/rubens_blog/venv/bin/python /srv/www/rubens_blog/rubens_blog/manage.py migrate

# restart gunicorn
echo "[EXECUTING COMMAND] systemctl reload gunicorn"
systemctl reload gunicorn

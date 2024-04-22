# This Folder contains files to setup the server. 

## How to setup
### Add a user for the ssh login
```
# set vi as editor, fix env language perl bug (https://stackoverflow.com/questions/2499794/how-to-fix-a-locale-setting-warning-from-perl)

echo "export EDITOR='vi'
export VISUAL='vi'
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8" >> ~/.bashrc

# set time & date 
timedatectl set-timezone Europe/Berlin


apt update && apt upgrade
# split package installation
apt-get install git postgresql postgresql-contrib nginx python3.11-venv python3-dev libpq-dev gcc

apt-get install unattended-upgrades
systemctl start unattended-upgrades
systemctl enable unattended-upgrades
unattended-upgrades --dry-run --debug
# where are the logs?


mkdir -p /srv/www/
cd /srv/www
git clone git@github.com:rubenvoss/rubens_blog.git
cd rubens_blog
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
export ENV_NAME=production

# make a webhook to automatically update Repo
apt install webhook
# test 
/usr/bin/webhook -hooks /srv/www/rubens_blog/install/hooks.json -verbose
# install service 
ln -s /srv/www/rubens_blog/production/webhook.service /etc/systemd/system/webhook.service
systemctl daemon-reload
systemctl enable webhook
systemctl start webhook
# where are the logs?

# back on local
rsync -r rubens_blog/rubens_blog/settings/*.py rubens-blog-production:/srv/www/rubens_blog/rubens_blog/rubens_blog/settings/

# back on prod
sudo -u postgres psql

https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457
CREATE DATABASE rubens_blog;
\connect rubens_blog
CREATE USER ruben WITH PASSWORD 'password';
# psql 15
CREATE SCHEMA rubens_blog_schema AUTHORIZATION ruben;
ALTER ROLE ruben SET client_encoding TO 'utf8';
ALTER ROLE ruben SET default_transaction_isolation TO 'read committed';
ALTER ROLE ruben SET timezone TO 'CET';
GRANT ALL PRIVILEGES ON DATABASE rubens_blog TO ruben;
ALTER DATABASE rubens_blog OWNER TO ruben;
# GRANT ALL ON SCHEMA public TO ruben;
# GRANT ALL ON SCHEMA public TO public;
\q

cat /usr/lib/systemd/system/postgresql.service
rsync install/postgresql.service rubens-blog-production:/usr/lib/systemd/system/postgresql.service
systemctl daemon-reload # load the updated service file from disk
systemctl enable postgresql
systemctl start postgresql
systemctl status postgresql
# where are the logs?


apt install ufw
ufw allow 80
# where are the logs?


# nginx
rsync install/nginx.conf rubens-blog-production:/etc/nginx/nginx.conf
systemctl enable nginx.service
systemctl start nginx
# where are the logs?



# gunicorn
rsync
systemctl daemon-reload
systemctl enable gunicorn
systemctl start gunicorn
# debug gunicorn
export ENV_NAME=production && cd /srv/www/rubens_blog/rubens_blog && ../venv/bin/gunicorn rubens_blog.wsgi -b 127.0.0.1:8000
# where are the logs?


cd /srv/www/rubens_blog/rubens_blog && export ENV_NAME=production && python manage.py runserver 0.0.0.0:80
cd /srv/www/rubens_blog/rubens_blog && export ENV_NAME=production && /srv/www/rubens_blog/venv/bin/gunicorn rubens_blog.wsgi
```

test23
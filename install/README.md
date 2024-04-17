# This Folder contains files to setup the server. 

## How to setup
### Add a user for the ssh login
```
echo "export EDITOR='vi'
export VISUAL='vi'
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8" >> ~/.bashrc

apt update && apt upgrade
apt-get install git postgresql postgresql-contrib nginx python3.11-venv python3-dev libpq-dev gcc

apt-get install unattended-upgrades
systemctl start unattended-upgrades
systemctl enable unattended-upgrades
unattended-upgrades --dry-run --debug

mkdir -p /srv/www/
cd /srv/www
git clone git@github.com:rubenvoss/rubens_blog.git
cd rubens_blog
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
export ENV_NAME=production

# back on local
rsync -r rubens_blog/rubens_blog/settings/*.py rubens-blog-production:/srv/www/rubens_blog/rubens_blog/rubens_blog/settings/

# back on prod
sudo -u postgres psql

https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457
CREATE DATABASE rubens_blog;
\c rubens_blog
CREATE USER ruben WITH PASSWORD 'password';
ALTER ROLE ruben SET client_encoding TO 'utf8';
ALTER ROLE ruben SET default_transaction_isolation TO 'read committed';
ALTER ROLE ruben SET timezone TO 'CET';
GRANT ALL PRIVILEGES ON DATABASE rubens_blog TO ruben;
ALTER DATABASE rubens_blog OWNER TO ruben;
GRANT ALL ON SCHEMA public TO ruben;
GRANT ALL ON SCHEMA public TO public;
\q

cat /usr/lib/systemd/system/postgresql.service
rsync install/postgresql.service rubens-blog-production:/usr/lib/systemd/system/postgresql.service
systemctl daemon-reload # load the updated service file from disk
systemctl enable postgresql
systemctl start postgresql
systemctl status postgresql

apt install ufw
ufw allow 80

cd /srv/www/rubens_blog/rubens_blog && export ENV_NAME=production && python manage.py runserver 0.0.0.0:80

```

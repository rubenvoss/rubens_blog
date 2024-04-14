# This Folder contains files to setup the server. 

## How to setup
### Add a user for the ssh login
```
echo "export EDITOR='vi'
export VISUAL='vi'
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8" >> ~/.bashrc

apt update && apt upgrade
apt-get install git postgresql nginx python3.11-venv

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
scp -r rubens_blog/rubens_blog/settings/ rubens-blog-production:/srv/www/rubens_blog/rubens_blog/rubens_blog

```
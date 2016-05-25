#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot < /home/box/web/etc/stepic.sql
/home/box/web/ask/manage.py syncdb
sudo ln -sf /home/box/web/etc/gunicorn.qa /etc/gunicorn.d/ask
sudo rm -rf /etc/gunicorn.d/*.example
cd ./web/ask
gunicorn --bind 0.0.0.0:8000 ask.wsgi 

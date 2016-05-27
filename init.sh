#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot < /home/box/web/etc/stepic.sql
/home/box/web/ask/manage.py syncdb
sudo rm -rf /etc/gunicorn.d/*.example
sudo cp /home/box/web/etc/django.example /etc/gunicorn.d/django.example
sudo /etc/init.d/gunicorn start

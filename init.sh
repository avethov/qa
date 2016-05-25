#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
mysql -uroot < /home/box/web/etc/stepic.sql
sudo ln -sf /home/box/web/etc/gunicorn.qa /etc/gunicorn.d/ask
sudo rm -rf /etc/gunicorn.d/*.example
sudo /etc/init.d/gunicorn restart

#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
if [ -d /data/web_static/current ]; then
    sudo rm -rf /data/web_static/current
fi
sudo symlink /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart

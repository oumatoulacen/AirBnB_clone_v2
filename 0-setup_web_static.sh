#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get -y install nginx
web_static_dir="/data/web_static/releases/test"
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Hello, this is a test HTML file." > "$web_static_dir/index.html"
ln -sf "$web_static_dir" /data/web_static/current
chown -R ubuntu:ubuntu /data/
old="server_name _;"
new="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|$old|$new|" /etc/nginx/sites-enabled/default
sudo service nginx restart

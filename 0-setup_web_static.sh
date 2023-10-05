#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories
web_static_dir="/data/web_static/releases/test"
shared_dir="/data/web_static/shared"

mkdir -p /data/web_static/{releases/test,shared}
touch "$web_static_dir/index.html"
echo "Hello, this is a test HTML file." > "$web_static_dir/index.html"

# Create or recreate symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -sf "$web_static_dir" /data/web_static/current

# Set ownership recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_text=$(cat <<EOL
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static/ {
        alias $shared_dir;
        expires 30d;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }

    error_page 500 502 503 504 /custom_50x.html;
    location = /custom_50x.html {
        root /usr/share/nginx/html;
        internal;
    }
}
EOL
)

echo "$config_text" > "$config_file"

# Restart Nginx
service nginx restart

echo "Web server setup completed."

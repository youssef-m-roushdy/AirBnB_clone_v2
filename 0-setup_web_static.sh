#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
<head><title>Test Page</title></head>
<body>
<h1>This is a test page for Nginx configuration.</h1>
<p>If you can see this, Nginx setup is successful!</p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create symbolic link, delete if already exists
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R yousef:yousef /data/

# Update Nginx configuration
sudo sed -i "/listen 80 default_server;/a \\
    location /hbnb_static/ {\\
        alias /data/web_static/current/;\\
    }" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

echo "Nginx setup completed."

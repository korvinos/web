sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-avilable/default
sudo ln -sf /home/korvinos/Documents/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/korvinos/Documents/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

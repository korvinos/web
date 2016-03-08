# Создаем базу данных MySQL
mysql -uroot -e "CREATE DATABASE box_django;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON box_django.* TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
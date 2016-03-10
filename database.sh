# Создаем базу данных MySQL
mysql -uroot -e "CREATE DATABASE web_test;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON web_test.* TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
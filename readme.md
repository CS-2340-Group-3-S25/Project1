### Django Setup:

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

### Load initial data:

- `python manage.py loaddata movies.json`
- `python manage.py loaddata reviews.json`

### Windows:

- winget install Oracle.MySQL
- pip install mysqlclient
- mysql -u root -p
- CREATE DATABASE movie_site_db;
- CREATE USER 'superuser'@'localhost' IDENTIFIED BY '';
- GRANT ALL PRIVILEGES ON movie_site_db.\* TO 'superuser'@'localhost';
- FLUSH PRIVILEGES;

### Mac:

- brew install mysql
- mysql -u root -p
- CREATE DATABASE movie_site_db;
- CREATE USER 'superuser'@'localhost' IDENTIFIED BY '';
- GRANT ALL PRIVILEGES ON movie_site_db.\* TO 'superuser'@'localhost';
- FLUSH PRIVILEGES;

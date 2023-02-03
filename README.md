# Set up environment
python version require: 3.5 or higher
install django 2.2.5 in MACOS/LINUX (might not work in version 3.x or higher)
```shell
pip install django==2.2.5
```

# Sever Startup guide
start at the path where django is installed
```shell
activate MyDjangoEnv
cd mysite
```

Before starting the server, register as superuser to see the posts
```shell
python manage.py createsuperuser
```
Signup your username, email, password to register as superuser
Start Server
```shell
python manage.py runserver
```
enter http://127.0.0.1:8000/ in browser to view
click right-up buttom to log in using the username and password registered earlier

# Application Description
database: sqlite3
framework: django

database structure:
Post:
| pk(primary key) | User   | author      | title      | text        | date         |
| -----------     | ------ | ----------- |----------- | ----------- |------------- |
|        0        | admin  | someone     | blog1      | blabla      |Fri Feb 2023  |

Comment:
| pk(primary key) | Post        | author     | text        | date         |
| -----------     | ----------- |----------- | ----------- |------------- |
|       0         |     0       | alp        | comment     |Fri Feb 2023  |

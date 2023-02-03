# Set up environment

python version require: 3.5 or higher

install django 2.2.5 in MACOS/LINUX (might not work in version 3.x or higher)

```shell
pip install django==2.2.5
```
install Anaconda for Virtual Environment Setup, ref: https://docs.anaconda.com/anaconda/install/mac-os/
## setup virtual Environment

```shell
conda create --name myDjangoEnv django=2.2
proceed ([y]/n)?
```

# Sever Startup guide
start at the path where django is installed (Linux/MACOS)
```shell
source activate MyDjangoEnv
cd mysite
```

Before starting the server, register as superuser to see the posts
(you can skip this step and use username:1 password:1 for later sign in)

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

Author relationships for each blog and comment is connected by the ForeignKey of Comment Class, Post and Comment have OneToMany relationship.

# Backend Comment APIs
the APIs for comment are in the file: /mysite/blog/models.py
In this file, Comment is defined as a class

## Add Comment
create a new comment object based on the post using django built-in api
```shell
get_object_or_404(Post, pk=pk)
```

## Delete Comment
Delete the Comment object in the database. Click the Delete button on the right-bottom side of comment to delete.
```shell
comment_object.delete()
```

## Approve Comment
After you submit your comment, you can approve that comment so that the server will confirm your comment and add 1 to the counter of the post you commented on. This works by setting approved_comment instance to be True or False.
Choose a button to keep or dump your new comment in the web app.
```shell
def approve(self):
    self.approved_comment = True
    self.save()
```

## Show Comment
In the website app, click on post title or comment counter to show all the comments

## Show comment date
This function is implemented using timezone api and store the date in the databse
```shell
created_date = models.DateTimeField(default=timezone.now)
```

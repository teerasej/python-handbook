
# Advanced ORM Techniques

## 1. Setup and run the project

1. Open `LabFiles_Advance/07-django-orm/project` in your editor.
2. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.
3. run `pip install -r requirements.txt` to install the required packages.
4. run `python manage.py migrate` to apply the migrations.
5. run `python manage.py runserver` to start the server.

## 2. Create models for the blog application

Open the `blog/models.py` file and define the following models:

```python
# blog/models.py
from django.db import models

# Define the Author model with the following fields:
class Author(models.Model):

    # - name: CharField with max length of 100 characters
    name = models.CharField(max_length=100)

    # override the __str__ method to return the name of the author
    def __str__(self):
        return self.name

# Define the Post model with the following fields:
class Post(models.Model):

    # - title: CharField with max length of 200 characters
    # - content: TextField, no length limit
    # - author: ForeignKey to the Author model with CASCADE delete behavior
    # - created_at: DateTimeField with auto_now_add=True, this field should be set when the record is created
    # - updated_at: DateTimeField with auto_now=True, this field should be updated every time the record is updated
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # override the __str__ method to return the title of the post
    def __str__(self):
        return self.title
```

## 3. Create and apply migrations

Back to the terminal (make sure you are in the `project` folder), run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 4.  Add some initial data using Django’s admin interface

Open the `blog/admin.py` file and register the models:

```python
# blog/admin.py
from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
```

## 5. Create a superuser

Run the following command in the terminal:

```bash
python manage.py createsuperuser
```

Fill in the required information to create a superuser.

## 6. Run the server and access the admin interface

Run the server using `python manage.py runserver` and access the admin interface at:

```
http://127.0.0.1:8000/admin/
```

then add some authors and posts.
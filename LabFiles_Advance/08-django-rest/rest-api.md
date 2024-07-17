# The REST API

## 1. Setup and run the project

1. Open `LabFiles_Advance/08-django-rest/project` in your editor.
2. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.
3. run `pip install -r requirements.txt` to install the required packages.
4. run `python manage.py migrate` to apply the migrations.
5. run `python manage.py runserver` to start the server.

## 2.  Create serializers for the models

create the new file: `blog/serializers.py` file and define the following serializers:

```python
# blog/serializers.py

# import the 'serializers' module from 'rest_framework', this module is used to serialize and deserialize data, ex. convert complex data types to native Python data types that can be rendered into JSON, XML, etc.
from rest_framework import serializers

# import the 'Author' and 'Post' models from the 'models' module
from .models import Author, Post

# Define the 'AuthorSerializer' class that inherits from 'serializers.ModelSerializer'
class AuthorSerializer(serializers.ModelSerializer):

    # The 'meta' class: used to define metadata for the serializer
    class Meta:
        # The 'model' attribute: specifies the model that the serializer should use to serialize/deserialize data
        model = Author
        # The 'fields' attribute: specifies the fields that should be serialized/deserialized
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    # The 'author' field: specifies that the 'author' field should be serialized using the 'AuthorSerializer'
    # the 'read_only' attribute is set to 'True' to indicate that the 'author' field is read-only
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
```

Save the changes and close the file.

## 3. Create API views

Open the `blog/views.py` file and define the following views:

```python
# blog/views.py
from rest_framework import viewsets
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer

# Define the 'AuthorViewSet' class that inherits from 'viewsets.ModelViewSet', this class provides the default 'create', 'retrieve', 'update', 'partial_update', 'destroy', and 'list' actions for the 'Author' model
class AuthorViewSet(viewsets.ModelViewSet):

    # The 'queryset' attribute: specifies the queryset that should be used to retrieve the 'Author' objects
    queryset = Author.objects.all()

    # The 'serializer_class' attribute: specifies the serializer class that should be used to serialize/deserialize the 'Author' objects
    serializer_class = AuthorSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Save the changes and close the file.

## 4. Register the API views in the `blog/urls.py` file

Create the `blog/urls.py` file and define the following URL patterns:

```python
# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PostViewSet

# Create a 'DefaultRouter' instance, this router will be used to automatically generate the URL patterns for the 'AuthorViewSet' and 'PostViewSet'
router = DefaultRouter()

# Register the 'AuthorViewSet' and 'PostViewSet' with the router, this will generate the URL patterns for the views like '/authors/'.
router.register(r'authors', AuthorViewSet)

# Register the 'PostViewSet' with the router, this will generate the URL patterns for the views like '/posts/'.
router.register(r'posts', PostViewSet)

# Define the URL patterns for the 'AuthorViewSet' and 'PostViewSet'
urlpatterns = [
    path('', include(router.urls)),
]
```

Save the changes and close the file.

## 5. Include the `blog` URLs in the project's `urls.py` file

Open the `blog_project/urls.py` file and include the `blog` URLs:

```python
# blog_project/urls.py
from django.contrib import admin

# Import the 'include' function from 'django.urls'
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the 'blog' URLs by adding the 'api/' prefix
    path('api/', include('blog.urls')),
]
```

Save the changes and close the file.

## 6. Run the server and test the API

Back to the terminal (make sure you are in the `project` folder), run the following commands:

```bash
python manage.py runserver
```

try to access the following URLs to ensure the application is working correctly:

```
http://127.0.0.1:8000/
```

## 7. Test the API using CURL or POSTman

You can test the API using CURL or POSTman. For this lab, we will use CURL.

### 7.1 CRUD with Author

1. Create an author:

```bash
curl -X POST http://127.0.0.1:8000/api/authors/ -H "Content-Type: application/json" -d "{\"name\":\"John Doe\"}"
```

For postman data:

```json
{
    "name": "John Doe"
}
```

2. Retrieve all authors:

```bash
curl -X GET http://127.0.0.1:8000/api/authors/
```

3. Update an author:

```bash
curl -X PUT http://127.0.0.1:8000/api/authors/1/ -H "Content-Type: application/json" -d "{\"name\":\"Jane Doe\"}"
``` 

For postman data:

```json
{
    "name": "Jane Doe"
}
```

4. **(Optional)** Delete an author:

```bash
curl -X DELETE http://127.0.0.1:8000/api/authors/1/
```

then check the result by retrieving all authors:

```bash
curl -X GET http://127.0.0.1:8000/api/authors/
```

### 7.2 CRUD with Post

1. (If you haven't created an author, create an author first)
2. Get an author ID from the previous step.
3. Create a post:

> Please noted that this example assumes that you have an author with ID 1.

```bash
curl -X POST http://127.0.0.1:8000/api/posts/ -H "Content-Type: application/json" -d "{\"title\":\"First Blog Post\", \"content\":\"This is the content of the first blog post.\", \"author\":1}"
```

For postman data:

```json
{
    "title": "First Blog Post",
    "content": "This is the content of the first blog post.",
    "author": 1
}
```

4. Retrieve all posts:

```bash
curl -X GET http://127.0.0.1:8000/api/posts/
```

5. Update a post:

```bash
curl -X PUT http://127.0.0.1:8000/api/posts/1/ -H "Content-Type: application/json" -d "{\"title\":\"Updated Blog Post Title\", \"content\":\"This is the updated content of the blog post.\", \"author\":1}"
```

For postman data:

```json
{
    "title": "Updated Blog Post Title",
    "content": "This is the updated content of the blog post.",
    "author": 1
}
```

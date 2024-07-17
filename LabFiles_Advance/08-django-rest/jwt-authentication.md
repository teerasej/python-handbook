
# Authentication with JWT

You have to finish the [REST API implementation](./rest-api.md) before you can start with this JWT authentication.

1. Open `LabFiles_Advance/08-django-rest/project` in your editor.
2. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.
3. run `pip install -r requirements.txt` to install the required packages.
4. run `python manage.py migrate` to apply the migrations.
5. run `python manage.py runserver` to start the server.

## 1. Install the required packages

Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.

```bash
pip install djangorestframework_simplejwt
```

## 2. Configure the project settings

Open the `project/settings.py` file and add the following configurations:

Start from the import statement:

```python
# blog_project/settings.py
from datetime import timedelta
```

then add the JWT settings:

```python
# blog_project/settings.py

# configure the JWT settings
REST_FRAMEWORK = {

    # This setting will allow the client to send the token in the Authorization header using the Bearer schema.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # This setting will require the client to authenticate before accessing the API.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```

Save the changes and close the file.

## 3. Create a custom permission class (optional)

You can create a custom permission class to allow only the author of the post to update or delete it.

Create a new file `blog/permissions.py` and add the following code:

```python
# blog/permissions.py

# BasePermission is a class provided by Django REST Framework that allows you to define custom permissions.
from rest_framework.permissions import BasePermission

# This permission class will allow only the author of the post to update or delete it.
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user
```

Save the changes and close the file.

## 4. Update the views to use JWT authentication and custom permissions

Open the `blog/views.py` file and update the views to use JWT authentication and the custom permission class.

```python
# blog/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # This will require the client to authenticate before accessing the Author API.
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # This will require the client to authenticate before accessing the Post API.
    # It will also use the custom permission class to allow only the author of the post to update or delete it.
    permission_classes = [IsAuthorOrReadOnly]
```

Save the changes and close the file.

## 5. Update the URLs routing to use JWT authentication

Open the `blog/urls.py` file and update the URLs routing to use JWT authentication.

```python
# blog/urls.py
from django.urls import path, include

# Import TokenObtainPairView and TokenRefreshView from rest_framework_simplejwt.views, these views will be used to obtain and refresh the JWT tokens.
# Django provides these views out of the box, so you don't need to create them manually.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include(router.urls)),

    # Add the URLs for obtaining and refreshing the JWT tokens.
    # the meaning of `token obtain pair` is to get the access token and refresh token.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # The refresh token URL will be used to refresh the access token.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Save the changes and close the file.

## 6. Test the JWT authentication using CURL or POSTman

You can test the API using CURL or POSTman. For this lab, we will use CURL.

1. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.

2. Run the following command to start the server:

```bash
python manage.py runserver
```
3. Try to create new author and post using the following CURL commands:

```bash
curl -X POST http://127.0.0.1:8000/api/authors/ -H "Content-Type: application/json" -d "{\"name\":\"John Doe\"}"
```

You will found the following error:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

4. obtain the access token and refresh token by sending a POST request to the `token/` URL:

> replace `testuser` and `testpassword` with the username and password of the superuser you created.

```bash
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d "{\"username\":\"testuser\", \"password\":\"testpassword\"}"
```

You will got the return message similar to these: 

```json
{
    "refresh": "eyJ0eXAiOiJK...", "access": "eyJ0eXAiOi..."
}
```

That's the token, in this lab you will use access token to access the API.

5. Try to create new author with the access by using the following CURL command:

> replace `<your_access_token>` with the access token you got from the previous step.

```bash
curl -X POST http://127.0.0.1:8000/api/authors/ -H "Content-Type: application/json"  -H "Authorization: Bearer <your_access_token>" -d "{\"name\":\"John Doe\"}"
```

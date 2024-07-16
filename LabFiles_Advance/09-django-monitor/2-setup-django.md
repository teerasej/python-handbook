
# Setup & test Sentry in Django

In this exercise, you will learn how to set up Sentry in a Django project to monitor the performance of your application.

## 1. Setup and run the project

1. Open the `LabFiles_Advance/09-django-monitor/project` in your editor.
2. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.
3. run `pip install -r requirements.txt` to install the required packages.
4. run `python manage.py runserver` to start the server.

## 2. (Optional) Install the Sentry SDK

If you haven't already installed the Sentry SDK, you can install it using the following command:

```bash
pip install --upgrade 'sentry-sdk[django]'
```

## 3. Configure Sentry in Django

1. Open the `blog_project/settings.py` file in your editor.

2. Add the following code snippet to the `settings.py` file to configure Sentry in your Django project:

> You can find your dns in the Sentry dashboard: `Projects (Left menu)` ->  `[Your Project]` -> `Settings` -> `SDK Setup` -> `Client Keys (DSN)`

```python
# settings.py
import sentry_sdk

#...

sentry_sdk.init(
    dsn="https://xxxxxx.ingest.us.sentry.io/xxxxxxx",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
```

Save the changes and close the file.

## 4. Add function to make error which will be catch by sentry

1. Open the `blog/views.py` file in your editor.
2. Add the following code snippet to the `views.py` file to create a function that will raise an error:

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
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
## Add the following function to the views.py file
def trigger_error(request):

    # This will raise an error that will be captured by Sentry
    division_by_zero = 1 / 0
```

Save the changes and close the file.

## 5. Add function to trigger by url request

1. Open the `blog/urls.py` file in your editor.
2. Add the following code snippet to the `urls.py` file to create a URL pattern that will trigger the error function:

```python
# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import  'trigger_error' function from the 'views' module, this function will be used to trigger an error
from .views import AuthorViewSet, PostViewSet, trigger_error

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Define the URL pattern for the 'trigger_error' function
    path('sentry-debug/', trigger_error),
]
```

3. Save the changes and close the file.

## 6. Test the Sentry integration

1. Right-click on the `project` folder and select `Open in Integrated Terminal` to open a terminal.
2. Run the following command to start the server:

```bash
python manage.py runserver
```

3. Open a web browser and navigate to http://127.0.0.1:8000/api/sentry-debug/
4. You should see an error page with the message `ZeroDivisionError at /api/sentry-debug/ division by zero`.
5. Go to the Sentry dashboard and check the performance monitoring data.
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
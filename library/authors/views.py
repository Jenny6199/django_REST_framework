from django.shortcuts import render
from rest_framework.views import ModelViewSet
from .model import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

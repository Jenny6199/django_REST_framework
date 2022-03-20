from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, ArticleModelSerializer, BookModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorSpecialViewSet(
    GenericViewSet, 
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin
):
    """
    Класс набора представлений для модели Author.
    Реализованы методы CRUD.
    """
    queryset = Author.objects.all()
    renderer_class = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = AuthorModelSerializer
    filterset_fields = ['last_name', 'first_name']


class BiographyModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Biography
    """
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BookModelViewSet(ModelViewSet):
    """
    Класс набора представлений для модели Book
    """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

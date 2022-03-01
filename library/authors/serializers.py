from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Article, Author, Biography, Book


class AuthorModelSerializer(HyperlinkedModelSerializer):
    """
    Сериализатор для модели Author,
    наследуется от HyperlinkedModelSerializer,
    поля - все поля модели автора.
    """
    class Meta:
        model = Author
        fields = '__all__'


class BiographyModelSerializer(ModelSerializer):
    """
    Сериализатор для модели Biography,
    наследуется от ModelSerializer,
    поля - text, author
    """
    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleModelSerializer(ModelSerializer):
    """
    Сериализатор для модели Article, 
    наследуется от ModelSerializer,
    поля - исключено поле name
    """
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        exclude = ['article_name']


class BookModelSerializer(ModelSerializer):
    """
    Сериализатор для модели Book,
    наследуется от ModelSerializer, 
    поля - все поля.
    """
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


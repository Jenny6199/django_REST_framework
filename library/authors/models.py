from django.db import models


class Author(models.Model):
    """
    Класс Автор
    Общая, простая модель автора книги\n
    ----------------------------------\n
    first_name - текст (макс.длина 64 символа)\n
    last_name - текст (макс.длина 64 символа)\n
    birthday_year - натуральное число\n
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

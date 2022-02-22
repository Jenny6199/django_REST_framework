from django.db import models
from uuid import uuid4

class Author(models.Model):
    """
    Класс Автор
    Общая, простая модель автора книги\n
    ----------------------------------\n
    uid - первичный ключ, UUID\n
    first_name - текст (макс.длина 64 символа)\n
    last_name - текст (макс.длина 64 символа)\n
    birthday_year - натуральное число\n
    ----------------------------------\n
    """
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

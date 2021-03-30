from django.db import models

from datetime import date


# Отзывы
class Review(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField("Имя", max_length=100, db_index=True)
    text = models.TextField("Сообщение", max_length=2500)
    date_pub = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.name

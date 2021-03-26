from django.db import models

from django.urls import reverse

from django.utils import timezone


class Room(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)

    slug = models.SlugField(max_length=150, unique=True,
                            help_text='Введите адрес, для товара. Адрес не может состоять из русский букв и символов, которые не поддерживаются браузерами')

    description = models.TextField(
        'Описание', help_text='Будет показано на странице номера')

    short_description = models.CharField(
        'Краткое описание', max_length=50, help_text='Будет показано на карточке номера')

    price = models.PositiveSmallIntegerField('Цена')

    size = models.PositiveSmallIntegerField('Размер команты')

    beds = models.PositiveSmallIntegerField('Количество кроватей')

    features = models.CharField(
        'Особенности', max_length=75, help_text='Например - беспроводной интернет и телевизор')

    poster = models.ImageField(
        'Картинка для карточки', null=True, upload_to='images/poster/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('room', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'комнату'
        verbose_name_plural = 'комнаты'


class Gallery(models.Model):
    image = models.ImageField(
        null=True, upload_to='images/gallery', default=None)

    text = models.CharField(
        'Текст на картинке', max_length=30, help_text='Текст будет поверх картинки')

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галерею'


class Image(models.Model):
    image = models.ImageField(null=True, upload_to='images/roomImages')
    room = models.ForeignKey(
        Room, default=None, related_name='room_image', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.room}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Review(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField("Имя", max_length=100, db_index=True)
    text = models.TextField("Сообщение", max_length=2500)
<<<<<<< HEAD
    date_pub = models.DateTimeField(default=date.today)
=======
    date_pub = models.DateTimeField(default=timezone.now)
>>>>>>> e33f757265b456d2b47205248700d7cbbd720f52

    def __str__(self):
        return self.name

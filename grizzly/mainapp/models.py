from django.db import models


class Room(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)

    slug = models.SlugField(max_length=150, unique=True,
                            help_text='Введите адрес, для товара. Адрес не может состоять из русский букв и символов, которые не поддерживаются браузерами')

    description = models.CharField(
        'Описание', max_length=150, help_text='Будет показано на странице номера')

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
        return {self.title}

    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'


class Gallery(models.Model):
    image = models.ImageField(
        null=True, upload_to='images/gallery', default=None)

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галерея'


class Image(models.Model):
    image = models.ImageField(null=True, upload_to='images/roomImages')
    room = models.ForeignKey(
        Room, default=None, related_name='room_image', on_delete=models.PROTECT)

    def __str__(self):
        return self.room

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

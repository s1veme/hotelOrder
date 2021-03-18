from django.db import models

        #Отзывы
class Reviews(models.Model): 
    email = models.EmailField(unique=True)
    name = models.CharField("Имя", max_length=100, db_index=True)
    text = models.TextField("Сообщение", max_length=5000)
    date_pub = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




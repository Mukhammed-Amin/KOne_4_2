from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField()
    image = models.ImageField(upload_to='infouser/', verbose_name="Фотография")
    work = models.CharField(max_length=255, verbose_name="Работа")
    description = models.TextField(verbose_name="Описание")
    twitter = models.URLField(verbose_name="Твиттер")
    telegram = models.URLField(verbose_name="Телеграм")
    linkedin = models.URLField(verbose_name="Линкед Ин")
    github = models.URLField(verbose_name="Гитхаб")
    
    def __str__(self):
        return f"{self.id} / {self.name} / {self.email} / {self.work}"
    
    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"
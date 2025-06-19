from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"
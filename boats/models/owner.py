from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=158, verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='почта')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

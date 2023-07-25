from django.db import models

from boats.models.owner import Owner

NULLABLE = {'blank': True, 'null': True}


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='год выпуска')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Лодка'
        verbose_name_plural = 'Лодки'


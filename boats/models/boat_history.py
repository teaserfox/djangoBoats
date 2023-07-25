from django.db import models
from boats.models.boat import Boat
from boats.models.owner import Owner

NULLABLE = {'blank': True, 'null': True}


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')
    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел с')
    stop_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел до')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.boat} {self.start_year} {self.stop_year}'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
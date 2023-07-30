from django.db import models


class City(models.Model):
    name = models.CharField("Название города", max_length=15)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

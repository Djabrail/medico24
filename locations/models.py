from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
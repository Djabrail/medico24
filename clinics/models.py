from django.db import models
from django.core.validators import RegexValidator
from locations.models import City


class ClinicService(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ClinicType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип учреждения'
        verbose_name_plural = 'Типы учреждениий'


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    type = models.ManyToManyField(ClinicType)
    service = models.ManyToManyField(ClinicService)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(null=True, blank=True, max_length=300, verbose_name="Улица")
    house_number = models.CharField(null=True, blank=True, max_length=300, verbose_name="Номер дома")
    phone = models.CharField(null=True, blank=True, max_length=16, verbose_name="Телефон",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'




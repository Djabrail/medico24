from django.shortcuts import reverse
from django.db import models
from users.models import User

from locations.models import City
from clinics.models import Clinic

from datetime import date

class Service(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('core:service', kwargs={'slug': self.slug})


class Rank(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квалификационная категория'
        verbose_name_plural = 'Квалификационные категории'


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    service = models.ManyToManyField(Service)
    rank = models.ForeignKey(Rank, null=True, blank=True, on_delete=models.CASCADE)
    clinic = models.ManyToManyField(Clinic)
    price = models.FloatField(verbose_name="Стоимость консультации", default=0)
    experience = models.CharField(max_length=300, verbose_name="Стаж")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Education(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_education', on_delete=models.CASCADE)
    date = models.CharField(max_length=100, verbose_name="Годы обучения", null=True, blank=True)
    description = models.TextField(verbose_name="Вуз и специальность", blank=True)
    position = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class Work(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_work', on_delete=models.CASCADE)
    date = models.CharField(max_length=100, verbose_name="Годы работы", null=True, blank=True)
    description = models.TextField(verbose_name="Место работы", blank=True)
    position = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Место работы'
        verbose_name_plural = 'Место работы'


def image_path(instance, filename):
    return '/'.join([str('users'), str(instance.id), str('diplom'), date.today().strftime('%Y/%m/%d'), filename])


class Diplom(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_diplom', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=image_path)
    position = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'



from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from datetime import date
from django.utils.text import slugify
from unidecode import unidecode

def image_path(instance, filename):
    return '/'.join([str('users'), str(instance.id), str('avatar'), date.today().strftime('%Y/%m/%d'), filename])

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    last_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    patronymic = models.CharField('Отчество', max_length=255, blank=True, null=True)
    full_name = models.CharField('ФИО', max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=250)
    phone = models.CharField(max_length=16,
                             verbose_name="Телефон",
                             unique=True,
                             validators=[
                                 RegexValidator(
                                     regex=r'^\+?1?\d{11,15}$',
                                     message="Телефонный номер должен быть в формате '+79999999999'."
                                 ),
                             ])
    image = models.ImageField(null=True, blank=True, upload_to=image_path, verbose_name="Фото")
    date_of_birth = models.DateField(verbose_name="Дата рождения",null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




    def save(self, *args, **kwargs):
        if self.first_name and self.last_name and self.patronymic:
            self.full_name = '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)
            self.slug = slugify(unidecode(u'{}-{}-{}-{}'.format(self.id, self.first_name, self.last_name, self.patronymic)))
        elif self.first_name and self.last_name:
            self.full_name = '{} {}'.format(self.first_name, self.last_name)
            self.slug = slugify(unidecode(u'{}-{}-{}'.format(self.id, self.first_name, self.last_name)))
        elif self.first_name:
            self.full_name = '{}'.format(self.first_name)
            self.slug = slugify(unidecode(u'{}-{}'.format(self.id, self.first_name)))
        else:
            self.full_name = self.phone
            self.slug = slugify(unidecode(u'{}-doctor'.format(self.id)))


        super(User, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if self.id:
    #         self.email = str('user{}@yandex.ru'.format(self.id))
    #     super(User, self).save(*args, **kwargs)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

from apps.users.managers import CustomUserManager
from apps.users.tasks import reset_password_message_sender


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Основной Email')
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    city = models.CharField(
        max_length=255,
        verbose_name='Город',
        blank=True, null=True,
    )
    postcode = models.CharField(
        max_length=255,
        verbose_name='Почтовый индекс',
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=13,
        blank=True, null=True,
        verbose_name='Номер телефона'
    )
    password_repeat = models.CharField(
        max_length=255, blank=True, null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('-id',)

    def __str__(self):
        return self.email


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "http://165.232.183.40/{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key)

    reset_password_message_sender.delay(email_plaintext_message, reset_password_token)

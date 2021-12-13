from django.db import models


class GetEmail(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новостная рассылка Email'
        verbose_name_plural = 'Новостные рассылки Email'
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.email


class MessageNewsletter(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'Информационный бюллетень'
        verbose_name_plural = 'Информационные бюллетени'
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.text[:10]

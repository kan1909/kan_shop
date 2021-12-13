from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.categories.models import Category


class MainPage(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Наименование',
        blank=True, null=True,
    )
    image = models.ImageField(
        upload_to='main_page',
        null=True, blank=True,
    )
    name = models.CharField(
        max_length=255, verbose_name='Наименование MainPage',
        blank=True,
    )
    categories = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='categories', blank=True, null=True,
    )

    class Meta:
        verbose_name = 'Главная Страница'
        verbose_name_plural = 'Главные Страницы'
        ordering = ('-id',)

    def __str__(self) -> str:
        return f"{self.title} -- {self.name} -- {self.categories}"


@receiver(post_save, sender=MainPage)
def create_category_name(sender, instance, created, *args, **kwargs):
    if created:
        instance.name = instance.title.lower().replace(' ', '_')
        instance.save()

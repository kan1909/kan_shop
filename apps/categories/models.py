from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(
        max_length=255, db_index=True,
        blank=True, null=True,
        verbose_name='Наименование категории'
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    name = models.CharField(
        max_length=255, verbose_name='Наименование Category',
        blank=True, db_index=True,
    )
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self) -> str:
        return f"{self.id} -- {self.title}"

    def save(self, *args, **kwargs):
        self.name = self.title.lower().replace(' ', '_')
        super(Category, self).save(*args, **kwargs)

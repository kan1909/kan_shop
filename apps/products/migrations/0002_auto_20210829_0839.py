# Generated by Django 3.2.5 on 2021-08-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='size_chart',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Размерная сетка'),
        ),
    ]

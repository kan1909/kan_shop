# Generated by Django 3.2.5 on 2021-08-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Стоимость'),
        ),
    ]
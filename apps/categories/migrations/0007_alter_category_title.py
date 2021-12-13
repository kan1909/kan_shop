# Generated by Django 3.2.5 on 2021-07-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='Наименование категории'),
        ),
    ]
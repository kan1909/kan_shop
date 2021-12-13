# Generated by Django 3.2.5 on 2021-08-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0007_alter_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='Артикль')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.category')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Наименование товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Стоимость')),
                ('quantity', models.PositiveIntegerField()),
                ('color', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Цвет')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='products.product')),
            ],
            options={
                'verbose_name': 'ПРОДУКТ',
                'verbose_name_plural': 'ПРОДУКТЫ',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='Изображение')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_image', to='products.productitem')),
            ],
        ),
    ]
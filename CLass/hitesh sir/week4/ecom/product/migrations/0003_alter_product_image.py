# Generated by Django 5.0.3 on 2024-04-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/product/p1.jpeg', upload_to='images/product_image'),
        ),
    ]

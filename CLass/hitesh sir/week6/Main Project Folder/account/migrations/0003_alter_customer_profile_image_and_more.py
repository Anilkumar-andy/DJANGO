# Generated by Django 5.0.6 on 2024-06-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customer_users_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(default='no image', upload_to='profile_image/'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company_logo',
            field=models.ImageField(default='no image', upload_to='logo/'),
        ),
    ]
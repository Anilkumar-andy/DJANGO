# Generated by Django 5.0.6 on 2024-06-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customer_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='document_photo',
            field=models.ImageField(default='no image', upload_to='documents'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
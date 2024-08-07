# Generated by Django 5.0.6 on 2024-06-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation', 'student')},
        ),
    ]

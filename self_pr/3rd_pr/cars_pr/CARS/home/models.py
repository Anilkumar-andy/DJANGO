from django.db import models

# Create your models here.
DRIVE_CHOICES = [
        ('FWD', 'Front Wheel Drive'),
        ('RWD', 'Rear Wheel Drive'),
        ('4WD', 'Four Wheel Drive'),
    ]
class Cars(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    drive_type = models.CharField(max_length=3, choices=DRIVE_CHOICES)
    image=models.ImageField(null=True,upload_to="car_img")
    desc=models.TextField()
    def __str__(self) -> str:
        return f"{self.name}"

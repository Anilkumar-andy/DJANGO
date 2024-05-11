from django.db import models

# Create your models here.
class Employee(models.Model):
    F_name=models.CharField(max_length=60)
    L_name=models.CharField(max_length=60)
    age=models.DecimalField(max_digits=5, decimal_places=2)
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
    profile_image=models.ImageField(null=True)
    file=models.FileField(null=True)

class Car(models.Model):
    c_name=models.CharField(max_length=90)
    speed=models.IntegerField(default=30)
    
    def __str__(self) -> str:
        return self.c_name
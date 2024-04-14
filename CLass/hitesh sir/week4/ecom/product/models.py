from django.db import models

CATEGORY_Choices=[
    ('ELECTRONICS','Electronics'),
    ('CLOTHING','Clothing'),
    ('BOOKS','Book')
]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    size = models.DecimalField(decimal_places=2,max_digits=4)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/product_image', default='images/product_image/p1.jpeg')
    category = models.CharField(max_length=45,choices=CATEGORY_Choices)
    weight = models.DecimalField(decimal_places=2,max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    def __str__(self) -> str:
        return f"name is {self.name} and price is {self.price}"

from attr import s
from django.db import models

# Create your models here.
class Review(models.Model):
    Author_Name = models.CharField(max_length=100, default='')
    Product_Name = models.CharField(max_length=150, default='')
    Product_Review = models.TextField(default='')
    Product_Image = models.ImageField(upload_to = 'productphotos')
    Time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Product_Name

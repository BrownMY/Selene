from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='products/', max_length=250, default='SOME STRING') 
    price = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    rating = models.IntegerField()
    imgurl = models.CharField(max_length=250)
    vidurl = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.my_float = round(self.my_float, 2)
        super(MyDataModel, self).save(*args, **kwargs)    
        
class Invoice(models.Model):
    
    total_cost = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.BooleanField()
    

def __str__(self):
    return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Invoice(models.Model):
    # user_id = models.IntegerField()
    total_cost = models.IntegerField()
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


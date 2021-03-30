from django.db import models


class User(models.Model):
    name = models.IntegerField()
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    subscription = models.BooleanField
    favorites = models.
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name


class Product(models.Model):
    name = models.IntegerField()
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name


class Product(models.Model):
    name = models.IntegerField()
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name


class Product(models.Model):
    name = models.IntegerField()
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    # this is associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name
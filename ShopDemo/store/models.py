from django.db import models
from django import forms


class Catrgory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Item(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey(Catrgory, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.Category

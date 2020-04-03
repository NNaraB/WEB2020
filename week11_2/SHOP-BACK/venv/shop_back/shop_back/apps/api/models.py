from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('name of the catgory', max_length=200)
    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField('name of the product', max_length = 200)
    price =  models.FloatField('price of the product')
    description = models.TextField('description of the product')
    count = models.IntegerField('number of products')
    def __str__(self):
        return  self.name
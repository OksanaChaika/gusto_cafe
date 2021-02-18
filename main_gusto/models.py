from django.db import models
from uuid import uuid4
from os import path


def get_file_name(self, filename):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return path.join('media/images/categories', filename)

def get_file_name2(self, filename):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return path.join('media/images/dishes', filename)

# Create your models here.
class Category(models.Model):


    title = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.title}:{self.category_order}'


class Dish(models.Model):
    title = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(upload_to=get_file_name2)
    dish_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.price}'


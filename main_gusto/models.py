from django.db import models
from uuid import uuid4
from os import path


def get_file_name(filename):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return path.join('media/images/categories', filename)



# Create your models here.
class Category(models.Model):


    title = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.title}:{self.category_order}'



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

def get_file_name3(self, filename):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return path.join('media/images/info', filename)

def get_file_name4(self, filename):
    ext = filename.strip().split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return path.join('media/images/team', filename)

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


class Info(models.Model):
    cafe_info = models.CharField(max_length=500, unique=True)
    photo = models.ImageField(upload_to=get_file_name3)
    is_visible = models.BooleanField(default=True)


class Team(models.Model):
    team_info = models.CharField(max_length=500, unique=True)
    photo = models.ImageField(upload_to=get_file_name4)
    is_visible = models.BooleanField(default=True)


class Phone(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.phone}'

class Address(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.CharField(max_length=5)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.city}; {self.street}; {self.home}'



class CafeInfo(models.Model):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)


class Message(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=400)

    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}:{self.user_email}:{self.user_message[:20]}'



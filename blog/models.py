from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import pre_save
from django.urls import reverse
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.TextField()
    fburl = models.CharField(max_length=300)
    twurl = models.CharField(max_length=300)
    inurl = models.CharField(max_length=300)
    yturl = models.CharField(max_length=300)
    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


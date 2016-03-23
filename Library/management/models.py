# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 自己需要看一下用 abstractuser 来集成的方法
class MyUser(models.Model):
    user = models.OneToOneField(User)
    # 额，暂时用数字来代替 permission
    permission = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length=128)
    pub_date = models.DateField()
    price = models.FloatField()
    author = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images')
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return self.name

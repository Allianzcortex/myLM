# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 一共要建立三个模型，包括：用户，图书，图片，

# 为用户分配不同的权限

class myUser(models.Model):
	user = models.OneToOneField(User)
	permission = models.IntegerField()

	def __unicode__(self):
		return self.user.username

class Book(models.Model):
	name = models.CharField(max_length=120)
	auth = models.CharField(max_length=40)
	pub_date = models.DateTimeField()
	price = models.FloatField()
	type = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

class Img(models.Model):
	book = models.ForeignKey(Book)
	img = models.ImageField(upload_to='image')
	desc = models.TextField()
	name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name



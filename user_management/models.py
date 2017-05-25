from __future__ import unicode_literals

# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import User
from models_fields_choices import USER_STATUS, GENDER
import random

# Create your models here.


class UserAccount(models.Model):
	user = models.OneToOneField(User)
	gender = models.CharField(max_length = 1, choices = GENDER)
	status = models.CharField(max_length =  1,choices = USER_STATUS)
	company = models.CharField(max_length = 10)


		

class Address(models.Model):
	user = models.ForeignKey('UserAccount')
	house_address = models.CharField(max_length=100)
	work_place = models.CharField(max_length = 100)
	local_government = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)
	state_of_origin = models.CharField(max_length=100)
		
		
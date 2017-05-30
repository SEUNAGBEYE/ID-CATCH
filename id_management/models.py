# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# from user_management.models import UserAccount

from django.contrib.auth.models import User

from model_field_choices import USER_STATUS, GENDER

# Create your models here.

class Id(models.Model):
	e_id = models.CharField(max_length = 11)
	created = models.DateTimeField()
	expires = models.DateTimeField()

	class Meta:
		verbose_name_plural = 'ID'


class UserAccount(models.Model):
	user = models.OneToOneField(User)
	user_eId = models.OneToOneField('Id', null=True)
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


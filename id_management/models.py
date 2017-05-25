# -*- coding: utf-8 -*-
import random

from __future__ import unicode_literals

from django.db import models

from user_management.models import UserAccount

# Create your models here.


class Id(models.Model):
	user = models.OneToOneField('UserAccount')
	e_id = models.CharField(max_length = 11, primary_key = True)
	created = models.DateTimeField()
	expires = models.DateTimeField()

	def gen_E_Id(self):

		e_id = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
		return e_id

class IdDraft(models.Model):
	user = models.OneToOneField('UserAccount')
	e_id = models.CharField(max_length = 11)
	created = models.DateTimeField()
	expires = models.DateTimeField()

	def gen_E_Id(self):

		e_id = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
		return e_id


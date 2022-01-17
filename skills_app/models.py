from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Updates(models.Model):
	email = models.CharField('email', max_length=120)
	
	
	def __str__(self):
		return self.email

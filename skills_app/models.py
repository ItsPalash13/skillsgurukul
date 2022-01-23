from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Email_list(models.Model):
    name = models.CharField('name', max_length=120)
    email = models.CharField('email', max_length=120)
    message = models.CharField('message', max_length=240)
	
	
	
    def __str__(self):
        return self.email

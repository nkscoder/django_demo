from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
     GENDER_CHOICES = (("M" ,"Male"),("F" ,"Female"))
     user = models.ForeignKey(User)
     gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="M")
     Age = models.IntegerField()
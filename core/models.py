from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (("M","MALE"),("F","FEMALE"))

    user = models.OneToOneField(User)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="M")
    Age = models.IntegerField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# from django.utils.encoding import python_2_unicode_compatible
# class Question(models.Model):
#     def __str__(self):
#         return self.question_text
#
# class Choice(models.Model):
#     def __str__(self):
#         return self.choice_text
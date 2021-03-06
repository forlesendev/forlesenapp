from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=200)

class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Learnt(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_word = models.ForeignKey(Word, on_delete=models.CASCADE)
    learnt = models.IntegerField(default=0)
    ok_rate = models.IntegerField(default=0)

class Input_text(models.Model):
    text = models.CharField(max_length=2000, default='')

class Input_word(models.Model):
    text_word = models.CharField(max_length=400, default='')

class Count_word(models.Model):
#    id_word = models.ForeignKey(Word, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

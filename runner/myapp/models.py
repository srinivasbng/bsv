# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField(max_length=200)
    age=models.IntegerField()

# Create your models here.

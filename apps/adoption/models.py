# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    home = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)


class Request(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True)
    number_pet = models.IntegerField()
    reasons = models.TextField()
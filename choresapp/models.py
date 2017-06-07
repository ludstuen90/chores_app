# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Chore(models.Model):
    chore_name = models.CharField(max_length=24)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.chore_name

    def __unicode__(self):
        return self.__str__()

class Boyfriend(models.Model):
    name = models.CharField(max_length=24, verbose_name="Name")
    email = models.EmailField(verbose_name="Email Address", max_length=64)
    phone = models.CharField(verbose_name="Phone Number", blank=False, max_length=24)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

class Clean(models.Model):
    chore_completed = models.ForeignKey(Chore, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    cleaner = models.ForeignKey(Boyfriend, on_delete=models.CASCADE)

    def __str__(self):
        return self.chore_completed.chore_name + ' ' +  self.cleaner.name

    def __unicode__(self):
        return self.__str__()

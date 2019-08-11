# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class words(models.Model):
    Column_2 = models.CharField(max_length=200,null= True)
    Column_3 = models.BigIntegerField(null=True)

    def __str__(self):
        return self.Column_2

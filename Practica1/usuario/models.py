# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Userf(User):
    carrera = models.CharField(max_length=30)
    CUI = models.CharField(max_length=13)
    User.username = models.CharField(primary_key=True)


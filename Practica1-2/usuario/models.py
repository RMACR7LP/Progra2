# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.encoding import force_unicode

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Texto(models.Model):
    nombre = models.CharField(max_length=225)
    archivo = models.FileField(blank=False,upload_to="textos",validators=[FileExtensionValidator(allowed_extensions=['pdf', 'pm2'])])
    autor = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre








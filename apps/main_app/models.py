from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User, UserManager
from datetime import datetime
import bcrypt
import re
# Create your models here.




class Item(models.Model):
    brand= models.CharField(max_length=80)
    date_add = models.DateTimeField()
    users = models.ManyToManyField(User, related_name = "items")
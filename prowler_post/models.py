from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class entry(models.Model):
    name = models.CharField(default = 'user',max_length= 20)
    text = models.TextField(max_length = 300)
    date_added = models.DateTimeField(auto_now_add=True)
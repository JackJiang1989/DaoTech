from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, DateField, DateTimeField

# Create your models here.

class Article(models.Model):
    author = CharField(max_length=10)
    content = CharField(max_length=100)
    date = DateTimeField()
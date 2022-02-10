from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    author = CharField(max_length=10)
    content = CharField(max_length=100)
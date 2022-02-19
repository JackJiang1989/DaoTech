from distutils.text_file import TextFile
from xmlrpc.client import DateTime
from django.db import models
# from django.forms import CharField, DateField, DateTimeField-

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length = 20)

class Author(models.Model):
    author = models.CharField(max_length = 20)


class Article(models.Model):
    # TAG=(
    #     ('heat transfer','ht'),
    #     ('mechine learning', '')
    #     ('cooking', 'co'),
    #     ('cycling', 'cy'),
    #     ('reading', 're')
    # )

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    content = models.TextField()
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)



class comments(models.Model):
    author = models.CharField(max_length = 20)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField()
    
    article = models.ForeignKey(
        Article,
        # verbose_name='文章',
        on_delete=models.CASCADE) 
        #Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.

    parent_comment = models.ForeignKey(
        'self',
        # verbose_name="上级评论",
        blank=True,
        null=True,
        on_delete=models.CASCADE)            



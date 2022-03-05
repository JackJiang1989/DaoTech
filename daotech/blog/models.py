from datetime import datetime
from distutils.text_file import TextFile
from xmlrpc.client import DateTime
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.urls import reverse
# from django.forms import CharField, DateField, DateTimeField-

# Create your models here.con

class Tag(models.Model):
    tag = models.CharField(max_length = 20)
    def __str__(self):
        return self.tag  

class Author(models.Model):
    author = models.CharField(max_length = 20)
    def __str__(self):
        return self.author  

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, default='')    
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    content = models.TextField()
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title  

class Comment(models.Model):
    author = models.CharField(max_length = 20, default='anonymous')
    email = models.EmailField(blank=True)
    # content = models.TextField()
    content = MarkdownxField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    article = models.ForeignKey(
        Article,
        # verbose_name='文章',
        on_delete=models.CASCADE) 
        #Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.

    # parent_comment = models.ForeignKey(
    #     'self',
    #     # verbose_name="上级评论",
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE) 

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return 'comment '+self.article.title + ' ' + self.author + ' {date}'.format(date=self.date)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"article_id": self.pk})


class Food(models.Model):
    name = models.CharField(max_length=50)
    taste = models.TextField()
    stars = models.PositiveSmallIntegerField()

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

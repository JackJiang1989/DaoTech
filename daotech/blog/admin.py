from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

from .models import Article, Author, Tag, Comment, Food, AboutMe

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Food)
admin.site.register(AboutMe)
# admin.site.register(MarkDownTest, MarkdownxModelAdmin)
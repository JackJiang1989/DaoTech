from markdownx.fields import MarkdownxFormField
from django import forms
from . import models


class MyForm(forms.Form):
    content_normal = forms.CharField(label = 'your_name', max_length=100)
    content_markdown = MarkdownxFormField()



class FoodForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = '__all__'
        # fields = ['name']
        # exclude = ['name']
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

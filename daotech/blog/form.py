from markdownx.fields import MarkdownxFormField
from django import forms
from . import models


class MyForm(forms.Form):
    content_normal = forms.CharField(label = 'your_name', max_length=100)
    content_markdown = MarkdownxFormField()

class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myfield in self.fields:
            print(myfield)
            self.fields[myfield].widget.attrs['class'] = 'form-control'
        # self.fields['position'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = models.Food
        fields = '__all__'
        # fields = ['name']
        # exclude = ['name']
        # widgets = {
        #     'name': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
        # }
        # widgets = {}

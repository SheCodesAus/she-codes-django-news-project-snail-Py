from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.utils import timezone, dateformat



class StoryForm(ModelForm):
     class Meta:
         model = NewsStory
         fields = "__all__"
        # fields = ['title', 'pub_date', 'content', 'tag', 'image']

         widgets = {'pub_date': forms.DateInput(format=('%Y-%m-%d'),
attrs={'class':'form-control', 'placeholder':'Select a date',
'type':'date', "value": dateformat.format(timezone.now(), 'Y-m-d')}),
}


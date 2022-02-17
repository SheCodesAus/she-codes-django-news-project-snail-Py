from django import forms
from django.forms import ModelForm
from .models import NewsStory
from datetime import datetime

class StoryForm(ModelForm):
     class Meta:
         model = NewsStory
         fields = ['title', 'pub_date', 'content', 'tag', 'image']
         widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'),
attrs={'class':'form-control', 'placeholder':'Select a date',
'type':'date'}),
}
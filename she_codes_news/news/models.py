from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class NewsStory(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey (
        get_user_model(),
        on_delete =models.CASCADE     # When killing the cat, don't forget to kill all the kittens as well

    )

    pub_date = models.DateTimeField(blank=True)

    content = models.TextField()

    tag_choices = (
       ("basic-feature", "Basic feature"),
        ("additional-feature", "Additional feature"),
        ("cool-stuff", "Cool stuff"),
        ("news", "News")
    )
   
    tag = models.CharField(max_length=200, choices = tag_choices, default="News")
    
    image = models.URLField(null=True, blank=True, default='https://picsum.photos/600')
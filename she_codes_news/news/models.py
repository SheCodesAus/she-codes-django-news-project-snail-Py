from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

class NewsStory(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey (
        get_user_model(),
        on_delete =models.CASCADE     # When deleting the cat, delete all the kittens

    )

    pub_date = models.DateTimeField(default=datetime.now)
    content = models.TextField()

    tag_choices = (
        ("Cats", "Cats"),
        ("Dogs", "Dogs"),
        ("News", "News")
    )
   
    tag = models.CharField(max_length=200, choices = tag_choices, default="News")

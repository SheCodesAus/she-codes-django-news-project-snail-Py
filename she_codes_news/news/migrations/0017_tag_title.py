# Generated by Django 4.0.1 on 2022-02-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_newsstory_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(default='news', max_length=200),
        ),
    ]

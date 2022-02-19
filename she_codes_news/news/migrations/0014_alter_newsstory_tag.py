# Generated by Django 4.0.1 on 2022-02-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_newsstory_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='tag',
            field=models.CharField(choices=[('basic-feature', 'Basic feature'), ('additional-feature', 'Additional feature'), ('cool-stuff', 'Cool stuff'), ('news', 'News')], default='News', max_length=200),
        ),
    ]
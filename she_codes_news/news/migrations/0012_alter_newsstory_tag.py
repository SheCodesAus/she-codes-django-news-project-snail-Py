# Generated by Django 4.0.1 on 2022-02-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_newsstory_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='tag',
            field=models.CharField(choices=[('Basic feature', 'Basic feature'), ('Additional feature', 'Additional feature'), ('Cool stuff', 'Cool stuff'), ('News', 'News')], default='News', max_length=200),
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_newsstory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, default='https://picsum.photos/600', null=True),
        ),
    ]
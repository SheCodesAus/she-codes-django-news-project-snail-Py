# Generated by Django 4.0.1 on 2022-02-17 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsstory_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

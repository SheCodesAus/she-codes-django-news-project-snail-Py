# Generated by Django 4.0.1 on 2022-02-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='tag',
            field=models.CharField(choices=[('Cats', 'Cats'), ('Dogs', 'Dogs'), ('News', 'News')], default='News', max_length=200),
        ),
    ]

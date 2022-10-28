# Generated by Django 4.1.1 on 2022-10-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deflor', '0004_women_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]

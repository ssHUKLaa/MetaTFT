# Generated by Django 4.1.7 on 2023-05-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topplayers', '0007_remove_matches_traits_traits'),
    ]

    operations = [
        migrations.AddField(
            model_name='champions',
            name='Rarity',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topplayers', '0005_rename_totaltier_traits_style'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traits',
            name='tierunits',
        ),
        migrations.AddField(
            model_name='traits',
            name='imageIcon',
            field=models.TextField(default='', max_length=100),
        ),
    ]
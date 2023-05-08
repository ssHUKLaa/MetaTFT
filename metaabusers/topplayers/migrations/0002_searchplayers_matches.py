# Generated by Django 4.1.7 on 2023-03-24 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topplayers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('playerId', models.CharField(max_length=200)),
                ('LP', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topplayers.players')),
                ('searchedPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topplayers.searchplayers')),
            ],
        ),
    ]
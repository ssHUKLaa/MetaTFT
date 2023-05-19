# Generated by Django 4.1.7 on 2023-05-19 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('matchID', models.CharField(default='tes', max_length=200, primary_key=True, serialize=False)),
                ('otherParticipants', models.CharField(default='', max_length=200)),
                ('placement', models.IntegerField(default=0)),
                ('game_time', models.CharField(default='', max_length=20)),
                ('game_length', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='searchPlayers',
            fields=[
                ('name', models.CharField(default='', max_length=200)),
                ('playerId', models.CharField(default='tes', max_length=200, primary_key=True, serialize=False)),
                ('LP', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('matchID', models.CharField(default='tes', max_length=200, primary_key=True, serialize=False)),
                ('traitname', models.CharField(default='', max_length=100)),
                ('currenttier', models.IntegerField(default=0)),
                ('tierunits', models.IntegerField(default=0)),
                ('associatedMatch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='topplayers.matches')),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='searchedPlayer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='topplayers.searchplayers'),
        ),
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('matchID', models.CharField(default='tes', max_length=200, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=20)),
                ('Star', models.IntegerField(default=1)),
                ('Items', models.CharField(default='', max_length=100)),
                ('Rarity', models.IntegerField(default=0)),
                ('associatedMatch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='topplayers.matches')),
            ],
        ),
    ]

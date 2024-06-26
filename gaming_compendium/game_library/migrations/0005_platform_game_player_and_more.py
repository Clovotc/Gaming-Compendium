# Generated by Django 5.0.2 on 2024-04-19 19:13

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_library', '0004_alter_game_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Singleplayer'), (2, 'Multiplayer'), (3, 'Both')], default=1),
        ),
        migrations.AddConstraint(
            model_name='platform',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='platform_name_case_insensitive_unique', violation_error_message='Platform already exists (case insensitive match)'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='game_library.platform'),
        ),
    ]

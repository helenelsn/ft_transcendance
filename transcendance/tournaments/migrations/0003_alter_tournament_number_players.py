# Generated by Django 4.2.16 on 2024-12-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_rename_end_tournament_over_remove_tournament_begin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='number_players',
            field=models.PositiveIntegerField(default=4),
        ),
    ]

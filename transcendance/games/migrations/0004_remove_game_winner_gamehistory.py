# Generated by Django 4.2.16 on 2024-12-12 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gamelaunching'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField()),
                ('left_score', models.PositiveIntegerField(default=0)),
                ('right_score', models.PositiveIntegerField(default=0)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
    ]
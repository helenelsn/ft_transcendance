# Generated by Django 4.2.16 on 2024-11-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_profile_friends'),
        ('games', '0002_delete_tournament_delete_tournamentplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.ManyToManyField(limit_choices_to=2, to='accounts.profile')),
            ],
        ),
    ]
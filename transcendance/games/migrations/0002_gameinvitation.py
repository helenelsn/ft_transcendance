# Generated by Django 4.2.16 on 2024-12-11 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInvitation',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.notification')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
            bases=('notifications.notification',),
        ),
    ]

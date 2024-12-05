# Generated by Django 4.2.16 on 2024-12-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0008_alter_relation_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='relation',
            field=models.IntegerField(choices=[(0, 'friend'), (1, 'friend_request'), (2, 'other_send_request'), (3, 'neutral'), (4, 'blocked')], default=3),
        ),
    ]

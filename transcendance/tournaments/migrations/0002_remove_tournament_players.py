# Generated by Django 4.2.16 on 2024-12-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='players',
        ),
    ]
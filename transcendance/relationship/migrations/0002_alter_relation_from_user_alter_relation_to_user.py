# Generated by Django 4.2.16 on 2024-12-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_notification'),
        ('relationship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='accounts.profile'),
        ),
    ]
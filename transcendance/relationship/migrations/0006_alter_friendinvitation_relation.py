# Generated by Django 4.2.16 on 2024-12-02 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0005_friendinvitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendinvitation',
            name='relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='relationship.relation'),
        ),
    ]
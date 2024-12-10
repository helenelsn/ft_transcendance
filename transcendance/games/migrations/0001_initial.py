# Generated by Django 4.2.16 on 2024-12-09 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Game!', max_length=30)),
                ('is_public', models.BooleanField(default=False)),
                ('left_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_player', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('right_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_player', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

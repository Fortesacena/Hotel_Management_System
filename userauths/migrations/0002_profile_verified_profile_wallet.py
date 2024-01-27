# Generated by Django 5.0.1 on 2024-01-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_profile_verified_profile_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identify_type',
            field=models.CharField(blank=True, choices=[('National Identification Number', 'National Identification Number'), ("Driver's Licence", "Driver's Licence"), ('International Passaport', 'International Passaport')], max_length=200, null=True),
        ),
    ]
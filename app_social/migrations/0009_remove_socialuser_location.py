# Generated by Django 5.1.4 on 2025-01-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0008_socialuser_age_socialuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialuser',
            name='location',
        ),
    ]

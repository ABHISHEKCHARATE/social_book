# Generated by Django 5.1.4 on 2025-01-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
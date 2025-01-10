# Generated by Django 5.1.4 on 2025-01-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0007_userfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='socialuser',
            name='date_of_birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]

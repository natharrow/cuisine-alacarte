# Generated by Django 2.2.7 on 2019-12-11 01:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesperson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='commission',
            field=models.FloatField(default=0.1, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(0.7)]),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-11 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesperson', '0002_salesperson_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='warnings',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]

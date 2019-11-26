# Generated by Django 2.2.7 on 2019-11-26 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('ssn', models.CharField(max_length=9)),
                ('salary', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('warnings', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)])),
            ],
        ),
    ]

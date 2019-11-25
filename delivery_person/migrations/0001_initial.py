# Generated by Django 2.2.7 on 2019-11-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('ssn', models.CharField(max_length=9)),
                ('warnings', models.IntegerField()),
                ('salary', models.FloatField()),
            ],
        ),
    ]

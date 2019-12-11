# Generated by Django 3.0 on 2019-12-10 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('customer', '0001_initial'),
        ('delivery_person', '0001_initial'),
        ('cook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('note', models.CharField(blank=True, default='', max_length=120)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Item')),
            ],
        ),
        migrations.CreateModel(
            name='DishRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('note', models.CharField(blank=True, default='', max_length=120)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('note', models.CharField(blank=True, default='', max_length=120)),
                ('delivery', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_person.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('note', models.CharField(blank=True, default='', max_length=120)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('note', models.CharField(blank=True, default='', max_length=120)),
                ('cook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cook.Cook')),
            ],
        ),
    ]

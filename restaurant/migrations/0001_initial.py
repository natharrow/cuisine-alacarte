# Generated by Django 2.2.7 on 2019-12-08 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Manager')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Dish')),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-04 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery_person', '0002_auto_20191204_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryperson',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.2.27 on 2022-03-07 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jwt',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='login_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
